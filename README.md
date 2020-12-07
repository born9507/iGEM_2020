# iGEM_2020 (KOREA_SIS)

> **공지사항**
>
> - Google Docs 에 정리되어 있는 내용을 바탕으로 웹페이지 제작
>
> - 페이지 수정 링크 https://2020.igem.org/Team:Korea-SIS 
> - CSS 파일 수정 링크: https://2020.igem.org/Template:Korea-SIS/CSS
> - JS 파일 수정 링크: https://2020.igem.org/Template:Korea-SIS/JS

## 1. 개요

iGEM 2020 대회 **연구 실적 정리** 위키 페이지 제작 외주

#### 사이트 URL 구조도

```http
https://2020.igem.org/Team:KOREA_SIS
https://2020.igem.org/Team:KOREA_SIS/Team
https://2020.igem.org/Team:KOREA_SIS/Project
https://2020.igem.org/Team:KOREA_SIS/Human_Practices
https://2020.igem.org/Team:KOREA_SIS/Awards
https://2020.igem.org/Team:KOREA_SIS/Safety
```



## 2. 일정

8/2 디자인 초안

**8월초**

html 내용 구조 추가

CSS 들어가기 전에 XD로 대강 디자인 컨셉을 잡아서 보여주고 수정할거있음 같이 수정해봅시다!

**8월말**

css 적용

**9월초**

자바스크립트 모션 등

**10월말**



## 3. 팁, 레이아웃

- https://2020.igem.org/Resources  //여기에 위키 작성법 등 정리되어 있음
  - [Telling Your Story](https://2020.igem.org/Resources/Telling_your_Story)
  - [Wiki Editing Help](https://2020.igem.org/Resources/Wiki_Editing_Help)
  - [Using HTML, CSS, and Javascript on Your Team Wiki](https://2020.igem.org/Resources/Using_HTML_CSS_and_Javascript)
  - [Template Documentation for Teams](https://2020.igem.org/Resources/Template_Documentation)



## 4. 참고 사이트

수상작 ( * 같은 디자인을 추구한다고 함 )

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

#### <방법 1> 이 방법을 쓰자!

html 소스 코드 내에 style 태그랑 script 태그 사용

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      h1 {
        color: blue;
      }
    </style>
  </head>
  <body>
    <input type="button" id="hw" value="Hello world" />
    <script type="text/javascript">
        var hw = document.getElementById('hw');
        hw.addEventListener('click', function(){
            alert('Hello world');
        })
    </script>
  </body>
</html>
```



#### <방법 2> 

CSS 파일, JS 파일 따로 업로드 하는 방법

##### 2020.igem.org/Template:TeamName/CSS

```css
<style>
/*Make text red and bold*/
.red_text {
    color: #f42434;
    font-weight:bold;
}
</style>
```

##### 2020.igem.org/Template:TeamName/JS

```js
<script>
$(document).ready(function() {
    $("#alert").addClass("red_text");
});
</script>
```

##### 2020.igem.org/Team:TeamName/Project

```html
{{TeamName/CSS}}
<html>
  <h2> Our Project </h2>
  <p> Beginning of the page about our project.</p>
</html>
{{TeamName/JS}}
```





#### 사진 업로드 방법

- 업로드 사이트 접속 https://2020.igem.org/Special:Upload

- **T--OFFICIAL team name--File_name** 의 형식으로 업로드

  ![img](https://2019.igem.org/wiki/images/7/7d/Uploading_a_file.png)

- ex)  T--Korea-SIS--photo.png 



#### 사진 html 에서 불러오기

URL이 어떤식으로 지정되지..? 이거 업로드 해봐야 알겠다.

```
<img src="image URL "> 
```

```
<video width="100%" height="240" controls>
<source src="https://2018.igem.org/wiki/images/f/fe/IGEM_Human_Practices.mp4" type="video/mp4">
</video>
```



### 그냥 참고



- Home
- Team
  - Team
  - Attributions
  - Collaborations
  - Inclusion
- Project
  - Contriubution
  - Description
  - Design
  - Engineering
  - Experiments
  - Notebook
  - Partnership
  - Proof of Concept
  - Results
- Parts
  - Part Collection
  - Parts
  - Improve
- Safety
- Human Practices
- Awards
  - Education
  - Entrepreneurship
  - Hardware
  - Measurement
  - Model
  - Plant
  - Software
  - Sustainable