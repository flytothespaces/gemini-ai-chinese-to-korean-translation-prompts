# Gemini AI Chinese-to-Korean Translation Prompts  

## 📌 Overview  
This repository provides a prompt example for using Gemini AI to translate  
from Chinese (CN) to Korean (KR).  
The translation workflow mainly relies on Colomo Translator.  
  
## 🚀 Features  
- A single prompt example (expandable in the future)  
- Focused on Chinese → Korean translation tasks  
- Easy to adapt for different contexts  
 
## 🛠 How to Use 
1. Clone the repository:  
   `bash  
   git clone https://github.com/flytothespaces/gemini-ai-chinese-to-korean-translation-prompts.git  
   `
2. Review the prompt in the prompts/ folder.  
3. Use with Gemini AI and Colomo Translator for translation tasks.
4. 콜로모 적용 설명.
   - 콜로모용 프롬프트 전체를 복사하여 붙여넣기.
   - 의역이 필요한 단어들 강제 의역 처리.
     * [Target_Semantic_Vocab]: []
       [] 대괄호 안에 ,로 구분하여 입력.
   - [Main Character]: 등장인물 정보 직접 입력하는 곳.
   - [Servant]: 등장인물 중 하인을 넣는 곳, 위 [Main Character] 블럭에 넣어도 무관하지만 여기에 넣어진 인물들은 기본적으로 등급이 낮게 설정됨.
   - [Main Character], [Servant] 블럭 사용법.
     * 해당 블럭 안에 아래 형식으로 데이터를 기입하여 사용. (다른 방법으로도 사용 가능).
       - CN:KR - GENDER, INFO1, INFO2, ... .
       또는
       - CN1:KR1, CN2:KR2, ... - GENDER, INFO1, INFO2, ... .
     * 예시:
          {```
          - 洪吉童:홍길동 - 남자, 주인공.
          - 洪吉順:홍길순, 吉順:길순 - 여자, 洪吉童의 여동생.
          ```}

   - [User-Defined Relationship Overrides] 블럭 사용법.
     * 인물들 사이의 말투를 사용자가 직접 입력하여 해당 말투를 유지하도록 유도하는 목적의 블럭임.
     * 해당 블럭 안에 아래 형식으로 데이터를 기입하여 사용. (다른 방법으로도 사용 가능).
       - CN -> CN: 좌측 CN이 우측 CN에게 사용할 대화체.
       또는
       - CN -> CN1, CN2, ...: 좌측 CN이 우측 CN1, CN2 등에게 사용할 대화체.
       또는
       - CN <-> CN: 좌우측 쌍방이 사용할 대화체.
     * 예시:
       {```
       # 1. 한 명이 여러 명에게 말할 때 (다중 청자)
       - 洪吉童 -> 洪吉順, 李道令: 친근한 하대 (Authoritative)

       # 2. 서로 같은 말투를 쓸 때 (상호 관계)
       - 洪吉童 <-> 金道令 : 평대 (Intimate Friend)
       - 士兵A <-> 士兵B : 평대 (Peer)

       # 3. 특정 1:1 관계
       - 洪吉順 -> 洪吉童 : 해요체 (Polite)
         ```}

   - [Vocabulary] 블럭 (단어장) 사용법.
     * 콜로모의 번역노트 입력란에 단어장 내용을 넣어둔다.
     * 해당 입력란 안에 아래 형식으로 데이터를 기입하여 사용. (다른 방법으로도 사용 가능).
       - CN:KR 좌측 CN에 매칭할 한국어.
       또는
       - CN:KR1 / KR2 / ... CN에 여러 한국어 매칭 후 문맥에 따라 선택하도록 할때.
     * 예시:
       {```
       - 洪吉童: 홍길동
       - 洪吉順: 홍길순 / 길순
       ```}
5. 일반 프롬프트 적용 설명.
   - 콜로모 설명과 동일하지만 일반용 프롬프트를 복사하여 붙여넣고, [Vocabulary] 블럭의 단어장 내용은 이 블럭에 직접 넣어야 함.
6. DB 블럭 입력시 주의사항.
   - 입력하는 모든 중국어는 원문 그대로 입력.
   - Simplified Chinese, Traditional Chinese 구분 확실히 해야 보다 정확하게 인식하여 처리됨.

## ⚠️ 면책 고지 (Disclaimer)
이 저장소는 저작권이 없는 중국어 원문을 번역하기 위한 프롬프트 자료를 제공합니다.  
본 프롬프트는 저작권이 없는 저작물에만 사용하도록 의도되었으며,  
저작권이 있는 저작물에 사용하는 것은 금지됩니다.  

이 프롬프트의 잘못된 사용, 비윤리적 활용, 저작권 침해, 또는 유해한 사용으로 인해 발생하는 모든 책임은 사용자에게 있습니다.  
저장소 소유자 및 기여자는 부적절하거나 불법적인 사용으로 인한 결과에 대해 어떠한 법적·윤리적 책임도 지지 않습니다.  

## ⚠️ Disclaimer
This repository provides prompt resources for translating Chinese texts that are free of copyright restrictions.  
These prompts are intended only for copyright-free works and must **not** be used with copyrighted materials.  

Any misuse, unethical application, copyright infringement, or harmful use of these prompts is the sole responsibility of the user.  
The repository owner(s) and contributors assume no legal or ethical liability for any outcomes resulting from improper or unlawful use.

## 📄 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

-----------------------------------------------------------
## 추가 내용 ##

## 💡 배경에 따른 교체 지시어
[4. Phase 2 - Step 2: Paraphrasing Process] 구절을 장르에 따라 아래 영문 문구들로 교체.
각 지시어는 AI가 해당 장르에 맞는 **어휘 사전(Lexicon)**을 선택하도록 설계되었습니다.

​1. 고대 배경 (무협, 언정소설, 선협)
​  - 특징: 한자어의 풍미를 살리되 문장은 유려하고 고풍스럽게 구성합니다.

        * [Paraphrasing Process]:
          - [Style Engine]: Classical/Archaic Wuxia Mode.
          - Logic: Paraphrase naturally to maintain an archaic/historical flavor, prioritizing the original intent and the elegant atmosphere of classical Chinese literature over literal translation.
          - Constraint: Strictly avoid modern Korean slang, loanwords, or overly localized idioms to preserve historical immersion. Ensure the dialogue reflects the appropriate social hierarchy and etiquette.
          ​- [Tone & Nuance Adaptation]:
​            * Focus: Classical elegance that bridges martial power and imperial grace. 
            * ​Primary Tone: Stoic, Elegant, and Rhythmic.
            * ​Nuance: Emphasize the poetic beauty of classical vocabulary. Maintain a disciplined, archaic flow that reflects traditional etiquette. Sentences should be fluid yet restrained, prioritizing metaphorical depth over literal emotional outbursts.
            * ​Hostile Nuance: Use 'Archaic Dignity & Sharp Coldness'. Express hostility through high-handed manners and elegant but lethal vocabulary. For palace strife, use indirect, sophisticated insults; for martial conflicts, use cold disdain for the opponent’s status or ability.

2. 현대 배경 (현대 판타지, 로맨스, 전문직물)
​  - 특징: 세련된 구어체와 트렌디한 어휘를 사용하여 가독성을 극대화합니다.

        * [Paraphrasing Process]:
          - [Style Engine]: Modern/Contemporary Mode.
          - Logic: Paraphrase naturally to maintain a modern and trendy flavor, prioritizing the original intent and contemporary sensibility over literal translation.
          - Constraint: Use polished, natural Korean dialogue styles (e.g., 해요체, 하십시오체) and idioms that reflect current social nuances. Avoid outdated or archaic phrasing that feels stiff in a modern setting.
          ​- [Tone & Nuance Adaptation]:
            * Focus: Vivid, trendy, and high-readability conversational style.
            * ​Primary Tone: Natural, Conversational, and Expressive.
            * ​Nuance: Fully adopt the rhythm of contemporary Korean speech. Focus on polished, trendy, and relatable dialogue styles. Ensure sentences are concise and impactful, reflecting modern social dynamics and emotional honesty.
            * ​Hostile Nuance: Use 'Sharp & Provocative Bluntness'. Utilize contemporary sarcasm and cold, cynical tones that target the opponent’s pride. Prioritize the raw, realistic tension found in modern noir or intense drama confrontations.

3. 미래/SF 배경 (사이버펑크, 스페이스 오페라, 가상현실)
  - ​특징: 기술적인 정교함과 차갑고 세련된 톤을 유지합니다.

        * [Paraphrasing Process]:
          - [Style Engine]: Futuristic/Sophisticated Tech Mode.
          - Logic: Paraphrase naturally to maintain a futuristic and sophisticated flavor, prioritizing the original intent and technological atmosphere over literal translation.
          - Constraint: Ensure technical terms feel integrated into a sleek, advanced society’s language. Maintain a sharp, precise, and professional narrative tone that suits a sci-fi environment.
​          ​- [Tone & Nuance Adaptation]:
            * Focus: Dry, analytical, and technologically sophisticated.
            * ​Primary Tone: Sharp, Precise, and Technocratic.
            * ​Nuance: Maintain a cool, rational atmosphere by minimizing emotional modifiers. Integrate technical jargon naturally into the prose to reflect an advanced society. Use punchy, noun-heavy sentence structures for a sleek, professional feel.
            * ​Hostile Nuance: Use 'Clinical Contempt'. Treat the opponent like a malfunctioning system or an obsolete relic. Express hostility through arrogant efficiency or robotic dismissiveness (e.g., treating human conflict as a mere calculation error).


4. 서양풍 판타지 (로판, 중세 판타지)
  - ​특징: 귀족적인 어투와 번역체 느낌이 없는 우아한 문체를 지향합니다.

        * [Paraphrasing Process]:
          - [Style Engine]: Western Fantasy/Aristocratic Mode.
          - Logic: Paraphrase naturally to maintain a classic Western fantasy atmosphere, prioritizing the elegant and formal tone of noble society.
          - Constraint: Use appropriate honorifics for aristocratic titles (e.g., 공작님, 영애). Avoid East Asian-specific idioms or modern slang that break the Western medieval/fantasy setting.
          ​- [Tone & Nuance Adaptation]:
            * Focus: Aristocratic grace and polished Western-style etiquette.
            * ​Primary Tone: Noble, Graceful, and Polished.
            * ​Nuance: Reflect the sophisticated social codes of Western aristocracy. Avoid 'Translationese' by using elegant, high-class Korean phrasing. Maintain an air of dignity even in casual dialogue, ensuring that every word reflects the character's status and education.
            * ​Hostile Nuance: Use 'Elegant Venom & Fantasy Elitism'. Insults should be sophisticated and reflect a sense of racial or bloodline superiority. Maintain a high-class vocabulary while delivering lethal, contemptuous strikes against the opponent's 'lowly' status or lack of power.





    

