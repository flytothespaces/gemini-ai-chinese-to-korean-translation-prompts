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

----------------------------------------------

## 📚 Public Domain & Open License Sources

아래 사이트들은 저작권이 만료되었거나 자유 라이선스로 공개된 원문을 제공하는 대표적인 아카이브입니다.  
저작권 걱정 없이 번역 연습이나 예시 자료로 활용할 수 있습니다.

- [Project Gutenberg](https://www.gutenberg.org/)  
  세계 최대의 퍼블릭 도메인 전자책 아카이브. 고전 문학과 다양한 언어 자료 제공.

- [Internet Archive](https://archive.org/)  
  책, 오디오, 영상 등 방대한 공공 자료를 무료로 열람 가능.

- [HathiTrust Digital Library](https://www.hathitrust.org/)  
  미국 대학 도서관들이 공동으로 제공하는 디지털 아카이브. 저작권 만료된 자료 다수 포함.

- [Google Books – Public Domain](https://books.google.com/)  
  저작권이 만료된 고전 서적을 무료로 다운로드할 수 있는 섹션 제공.

- [국립중앙도서관 디지털컬렉션](https://www.nl.go.kr/)  
  한국 내 저작권 만료 자료 및 고서 디지털화 제공.

- [中文维基百科 (Chinese Wikipedia)](https://zh.wikipedia.org/)  
  CC BY-SA 라이선스로 공개된 중국어 위키백과 문서. 자유롭게 번역·재사용 가능하나  
  **저작자 표시(Attribution)**와 **동일조건변경(ShareAlike)** 의무가 있습니다.

⚠️ **주의사항**  
- 각 사이트의 라이선스 안내를 반드시 확인하세요.  
- 일부 자료는 국가별 저작권법 차이로 보호 여부가 달라질 수 있습니다.  
- 번역·재배포 시 출처 표기를 권장합니다.
