# 여러 번역 비교하기 귀찮아서 만든 프로젝트
여러 사이트의 번역(Google, Papago,...) 을 비교하는데 브라우저 창 이동하기 귀찮아요. 한 번에 비교해서 보기 위해 만들었습니다. 영한 기술 번역을 하고 있습니다. 저는 초벌번역을 자동번역으로 하고 이후에 수정하면서 번역합니다. 번역을 조금 더 매끄럽게 하기 위해, 같은 글을 영어 외 다른 언어로 된 번역된 글도 참고 합니다. 도구이니 최대한 적은 시간을 들여 간단하게 만들 겁니다.

## 요구사항
### Version 01
- 여러 번역 API 의 번역 결과가 한 눈에 보임
  - Google, Papago, AWS, Kakao, Azure
- 영한 번역 외에 다른 나라 언어(중국어, 일본어,...) 도 번역할 수 있어야함
  - 같은 리포지토리에 여러 언어가 폴더 또는 브랜치만 다르게 해서 같은 아티클로 구성되어있다면 하나의 링크를 
- 무료이거나 최대한 돈을 절약할 수 있는 구성
- 번역해야할 텍스트는 500자 내(문단 단위로 쪼개서 번역)

### Ver02
- 링크를 입력해 링크에 있는 본문 번역


## 구성
### Version 01
- Front : Bootstrap 
- Backend : Flask
- API : [googletrans](https://py-googletrans.readthedocs.io/en/latest/), [PAPAGO 번역](https://developers.naver.com/products/nmt/), [PAPAGO 언어감지](https://developers.naver.com/products/detectLangs/) 
- Infra : GCP GCE([항상 무료 사용한도](https://cloud.google.com/free/docs/gcp-free-tier?hl=ko)) / Ubuntu 16.04 LTS
- Server : Flask 내장 서버 또는 Nginx

### Version 02
- 써보고 싶은 기술스택

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.
