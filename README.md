# iGEM_2020 (KOREA_SIS)

> **공지사항**
>
> - Google Docs 에 정리되어 있는 내용을 바탕으로 웹페이지 제작
>
> - 페이지 링크 https://2020.igem.org/Team:Korea-SIS 
> - CSS 링크: https://2020.igem.org/Template:Korea-SIS/CSS
> - JS 링크: https://2020.igem.org/Template:Korea-SIS/JS



## 1. 개요

iGEM 2020 대회 **연구 실적 정리** 위키 페이지 제작 외주



## 2. 일정

**8월초**

- 디자인 초안(Adobe XD)

- html 내용 구조 추가

**8월말**

- css, 자바스크립트 적용

**9월초**

- 계속해서 페이지 내용 세부 수정(Google doc 변경사항에 맞춰서)



## 3. 팁, 레이아웃

- https://2020.igem.org/Resources  //여기에 위키 작성법 등 정리되어 있음
  - [Telling Your Story](https://2020.igem.org/Resources/Telling_your_Story)
  - [Wiki Editing Help](https://2020.igem.org/Resources/Wiki_Editing_Help)
  - [Using HTML, CSS, and Javascript on Your Team Wiki](https://2020.igem.org/Resources/Using_HTML_CSS_and_Javascript)
  - [Template Documentation for Teams](https://2020.igem.org/Resources/Template_Documentation)



## 4. 참고 사이트

수상작 ( * 같은 디자인을 추구 )

https://2019.igem.org/Team:Mingdao  *

https://2019.igem.org/Team:Lambert_GA  *

https://2019.igem.org/Team:GreatBay_SZ



한국팀

https://2019.igem.org/Team:Korea_HS

https://2019.igem.org/Team:SIS_Korea



기타 참고작

https://2019.igem.org/Team:TU_Kaiserslautern/Parts



## 5. 업로드 방법

#### 페이지 업로드 방법

- https://2020.igem.org/Team:Korea-SIS  에 접속
- 로그인
- wiki tools - Edit
- html 소스 코드 수정하면 된다!



#### CSS, JS 파일 적용 방법 

##### 2020.igem.org/Template:Korea-SIS/CSS

- CSS 는 iGEM 자체 CSS 를 덮어씌워야 함(그냥 하면 원하는 레이아웃이 나오지 않는다)

```css
/* ---------기본 설정 -------------------------------------- */
#sideMenu, #top_title, .patrollink, #firstHeading, #home_logo, #sideMenu {
    display:none; 
}
#content { 
    padding:0px; 
    width:100%; 
    margin-top:-7px; 
    margin-left:0px; 
    border:none;
}
body, html {
    background-color:white; 
    width: 100%; 
    height: 100%;
}
#bodyContent h1, #bodyContent h2, #bodyContent h3, #bodyContent h4, #bodyContent h5 { 
    margin-bottom: 0px; 
}
#bodyContent a[href ^="https://"], .link-https { 
    padding-right:0px;
}
```

- 아래는 css 업로드 예제

```css
.red_text {
    color: #f42434;
    font-weight:bold;
}
```

##### 2020.igem.org/Template:Korea-SIS/JS

```js
$(document).ready(function() {
    $("#alert").addClass("red_text");
});
```

##### 2020.igem.org/Team:Korea-SIS/<doc_name>

```html
<html>
    <head>
	    <link rel="stylesheet" type="text/css" href="https://2020.igem.org/wiki/index.php?title=Template:Korea-SIS/CSS&action=raw&ctype=text/css" />    
    </head>
	<body>
        
		<script type="text/javascript" src="https://2020.igem.org/wiki/index.php?title=Template:Korea-SIS/JS&action=raw&ctype=text/javascript"></script>
    </body>
</html>
```



#### 사진 업로드 방법

- 업로드 사이트 접속 https://2020.igem.org/Special:Upload

- **T--OFFICIAL team name--File_name** 의 형식으로 업로드

  ![img](https://2019.igem.org/wiki/images/7/7d/Uploading_a_file.png)

- ex)  T--Korea-SIS--photo.png 



#### 사진 html 에서 불러오기

- 업로드 후 사진 원본 url 복사해서 링크

```
<img class="background-image" src="https://2020.igem.org/wiki/images/1/1f/T--Korea-SIS--background.png"/>
```

```
<video autoplay muted controls width="800px" height="auto" src="https://2020.igem.org/wiki/images/c/ce/T--Korea-SIS--attribution_video.mp4"></video>
```
