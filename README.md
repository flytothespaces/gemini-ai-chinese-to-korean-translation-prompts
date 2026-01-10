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
   git clone https://github.com/thinksys-JS/gemini-ai-chinese-to-korean-translation-prompts.git  
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
   - 콜로모 설명과 동일하지만 [Vocabulary] 블럭의 단어장 내용은 이 블럭에 직접 넣어야 함.
## 🤝 Contributing  
Contributions are welcome!  
Feel free to open issues or submit pull requests to add more prompt examples.  

## ⚠️ Disclaimer
This repository provides prompt resources for translation tasks.  
Any misuse, unethical application, or harmful use of these prompts is the sole responsibility of the user.  
The author(s) assume no liability for outcomes resulting from improper use.

## 📄 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
