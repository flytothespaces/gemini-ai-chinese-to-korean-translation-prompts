import re
import chardet
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.screenmanager import ScreenManager, Screen

# ---------- 유틸 함수 ----------
def read_text_with_autodetect(file_path):
    with open(file_path, "rb") as f:
        raw = f.read()
    enc = chardet.detect(raw)["encoding"]
    tried_encodings = [enc, "utf-8", "cp949", "gb18030", "gbk"]
    for e in tried_encodings:
        if not e:
            continue
        try:
            return raw.decode(e)
        except:
            continue
    return raw.decode(enc or "utf-8", errors="ignore")

# ---------- 병합 화면 ----------
class MergeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.filechooser = FileChooserListView(multiselect=True, filters=["*.txt"])
        layout.add_widget(self.filechooser)

        self.group_input = TextInput(hint_text="묶음 크기 입력", multiline=False)
        layout.add_widget(self.group_input)

        self.output_input = TextInput(hint_text="출력 파일 이름 입력", multiline=False)
        layout.add_widget(self.output_input)

        merge_btn = Button(text="병합 실행")
        merge_btn.bind(on_press=self.merge_files)
        layout.add_widget(merge_btn)

        back_btn = Button(text="메인으로")
        back_btn.bind(on_press=lambda x: self.manager.current = "main")
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def merge_files(self, instance):
        files = self.filechooser.selection
        if not files:
            return
        try:
            group_size = int(self.group_input.text)
        except:
            return
        output_base = self.output_input.text.strip()
        if not output_base:
            return

        for i in range(0, len(files), group_size):
            group = files[i:i+group_size]
            output_filename = f"{output_base}_{i//group_size}.txt"
            with open(output_filename, "w", encoding="utf-8") as outfile:
                for file in group:
                    with open(file, "r", encoding="utf-8", errors="ignore") as infile:
                        outfile.write(infile.read())
                        outfile.write("\n")
        print("병합 완료!")

# ---------- 분할 화면 ----------
class SplitScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        self.filechooser = FileChooserListView(multiselect=False, filters=["*.txt"])
        layout.add_widget(self.filechooser)

        self.pattern_input = TextInput(hint_text="분할 기준 정규식 입력", multiline=False)
        layout.add_widget(self.pattern_input)

        self.output_input = TextInput(hint_text="출력 파일 이름 입력", multiline=False)
        layout.add_widget(self.output_input)

        split_btn = Button(text="분할 실행")
        split_btn.bind(on_press=self.split_file)
        layout.add_widget(split_btn)

        back_btn = Button(text="메인으로")
        back_btn.bind(on_press=lambda x: self.manager.current = "main")
        layout.add_widget(back_btn)

        self.add_widget(layout)

    def split_file(self, instance):
        file_path = self.filechooser.selection[0] if self.filechooser.selection else None
        if not file_path:
            return
        pattern = self.pattern_input.text.strip()
        if not pattern:
            return

        text = read_text_with_autodetect(file_path)
        parts = re.split(f"({pattern})", text)

        chapter_texts = []
        current = ""
        for part in parts:
            if re.match(pattern, part):
                if current:
                    chapter_texts.append(current)
                current = part
            else:
                current += part
        if current:
            chapter_texts.append(current)

        base_name = self.output_input.text.strip()
        for idx, chapter in enumerate(chapter_texts, start=0):  # 0번부터 저장
            output_filename = f"{base_name}_{idx}.txt"
            with open(output_filename, "w", encoding="utf-8") as outfile:
                outfile.write(chapter)
        print("분할 완료!")

# ---------- 메인 화면 ----------
class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        merge_btn = Button(text="병합 기능")
        merge_btn.bind(on_press=lambda x: self.manager.current = "merge")
        layout.add_widget(merge_btn)

        split_btn = Button(text="분할 기능")
        split_btn.bind(on_press=lambda x: self.manager.current = "split")
        layout.add_widget(split_btn)

        self.add_widget(layout)

# ---------- 앱 ----------
class TextToolApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(MergeScreen(name="merge"))
        sm.add_widget(SplitScreen(name="split"))
        return sm

if __name__ == "__main__":
    TextToolApp().run()
