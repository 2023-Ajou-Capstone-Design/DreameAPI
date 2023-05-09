# DreameAPI

접근 URL : http://3.130.31.88:5000

## 지도
### 마커 띄우기
호출 URL : POST http://3.130.31.88:5000/map/MyPosition?myPositionLng=127.043517&myPositionLat=37.28224800000001&mbr=5000  
결과 예시 : 
```json
{
	"items": [
		{
			"Distance": 4689.286047055654,
			"StoreID": 5423,
			"StoreName": "빵으로 태어날걸",
			"StorePointLat": 37.2492,
			"StorePointLng": 127.076,
			"StoreType": "1"
		}
	],
	"total": 1
}
```

### 카테고리 선택시
#### 대분류 카테고리 선택
호출 URL : POST http://3.130.31.88:5000/map/Choose/Category?Category=2&myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000  
결과예시 : 
```json
{
	"items": [
		{
			"CateName": "마트",
			"Category": "2",
			"Distance": 91.6549791856995,
			"StoreID": 8213,
			"StoreName": "씨유(CU) 아주대일신관점",
			"StorePhoto": "",
			"StorePointLat": 37.28305638,
			"StorePointLng": 127.043660039,
			"StoreType": "1",
			"SubCateName": "편의점",
			"SubCategory": "2"
		}
	],
	"total" : 1
}
```
#### 소분류 카테고리 선택
호출 URL : POST http://3.130.31.88:5000/map/Choose/SubCategory?Category=2&SubCategory=2&myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000  
결과 예시 :
```json
{
	"items": [
		{
			"CateName": "마트",
			"Category": "2",
			"Distance": 91.6549791856995,
			"StoreID": 8213,
			"StoreName": "씨유(CU) 아주대일신관점",
			"StorePhoto": "",
			"StorePointLat": 37.28305638,
			"StorePointLng": 127.043660039,
			"StoreType": "1",
			"SubCateName": "편의점",
			"SubCategory": "2"
		}
	],
	"total" : 1
}

```

#### 가게유형 선택
호출 URL : POST http://3.130.31.88:5000/map/Choose/StoreType?StoreType=1&myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000  
결과 예시 :
```json
{
	"items": [
		{
			"CateName": "식음료",
			"Category": "1",
			"Distance": 91.6549791856995,
			"StoreID": 8209,
			"StoreName": "만권화밥 아주대학교점",
			"StorePhoto": "",
			"StorePointLat": 37.28305638,
			"StorePointLng": 127.043660039,
			"StoreType": "1",
			"SubCateName": "기타",
			"SubCategory": "99"
		}
	],
	"total" : 1
}

```
### 키워드 검색
호출 URL : http://3.130.31.88:5000/map/KeywordSearch?myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000&Keyword=%EC%8A%A4%EC%8B%9C  
결과 예시 :
```json
{
	"items": [
		{
			"CateName": "식음료",
			"Category": "1",
			"Distance": 4688.589533690853,
			"StoreID": 7276,
			"StoreName": "(주)스시타이쇼",
			"StorePhoto": "",
			"StorePointLat": 37.2492,
			"StorePointLng": 127.076,
			"StoreType": "1",
			"SubCateName": "기타",
			"SubCategory": "99"
		}
	],
	"total" : 1
}
```

### 마커 클릭 혹은 가게 클릭시
호출 URL : http://3.130.31.88:5000/map/StoreDetail?StoreID=1&StoreType=1&UserID=Tester  
결과 예시 :  
```json
{
	"items": [
		{
			"Address": "경기도 수원시 장안구 팔달로 273",
			"CateName": "식음료",
			"DayFinish": "0:00:00",
			"DayStart": "0:00:00",
			"DetailAddress": "",
			"HoliFinish": "0:00:00",
			"HoliStart": "0:00:00",
			"Item": "",
			"Phone": "0507-1348-7079",
			"Provided1": "",
			"Provided2": "",
			"SatFinish": "0:00:00",
			"SatStart": "0:00:00",
			"StoreID": 1,
			"StoreName": "보용만두",
			"StorePhoto": "",
			"StorePointLat": 37.28969219,
			"StorePointLng": 127.0146461,
			"StoreType": "1",
			"SubCateName": "기타",
			"WorkDay": "",
			"Bookmarked":1
		}
	],
	"total": 1
}
```


## 푸드쉐어링
### 글등록
호출 URL : http://3.130.31.88:5000/FoodShare/add?UserID=Tester&Title=test%EC%9E%85%EB%8B%88%EB%8B%A4.2&contents=%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%A4%91%EC%9D%B4%EC%97%90%EC%9A%94.%20%EB%A7%9B%EB%82%9C%EA%B1%B0%20%EB%A7%8E%EC%9D%B4%20%EB%A8%B9%EC%96%B4%EC%9A%94&Photo1&Photo2&Photo3&Town=%EC%88%98%EC%9B%90%EC%8B%9C%20%EC%98%81%ED%86%B5%EA%B5%AC%20%EC%9B%90%EC%B2%9C%EB%8F%99
결과예시 : sucess

### 글삭제
호출 URL : http://3.130.31.88:5000/FoodShare/del?UserID=Tester&WritingID=2023-04-09%2012%3A32%3A32.0000  
결과예시 : sucess

### 글상세
호출 URL : http://3.130.31.88:5000/FoodShare/Detail?UserID=Tester&WritingID=2023-04-09%2012%3A33%3A31.0000  
결과예시 : 
```json
{
	"items": [
		{
			"Contents": "None",
			"Photo1": "",
			"Photo2": "",
			"Photo3": "",
			"Title": "test입니다.",
			"Town": "",
			"UploadTime": "2023-04-10 20:57:04",
			"UserID": "Tester",
			"WritingID": "2023-04-10 20:57:04"
		}
	],
	"total": 1
}
```

### 글 수정
호출 URL : http://3.130.31.88:5000/FoodShare/Modify?UserID=Tester&Title=test%EC%9E%85%EB%8B%88%EB%8B%A4.&contents=%ED%85%8C%EC%8A%A4%ED%8A%B8%20%EC%A4%91%EC%9D%B4%EC%97%90%EC%9A%94.%20%EB%A7%9B%EB%82%9C%EA%B1%B0%20%EB%A7%8E%EC%9D%B4%20%EB%A8%B9%EC%96%B4%EC%9A%94&Photo1&Photo2&Photo3&WritingID=2023-04-10%2020%3A57%3A04.0000&Town=%EC%88%98%EC%9B%90%EC%8B%9C%20%EC%98%81%ED%86%B5%EA%B5%AC%20%EC%9B%90%EC%B2%9C%EB%8F%99  
결과 예시 : sucess  

### 글 조회
호출 URL : http://3.130.31.88:5000/FoodShare/getList?Town=%EC%88%98%EC%9B%90%EC%8B%9C%20%EC%98%81%ED%86%B5%EA%B5%AC%20%EC%9B%90%EC%B2%9C%EB%8F%99  
결과 예시 :
```json
{
	"items": [
		{
			"Photo1": "",
			"Title": "test입니다.",
			"Town": "수원시 영통구 원천동",
			"UploadTime": "2023-04-11 03:51:02",
			"UserID": "Tester",
			"WritingID": "2023-04-10 20:57:04"
		}
	],
	"total": 1
}
```

## 마이페이지
### 내가 쓴글
호출 URL : http://3.130.31.88:5000/MyPage/myList?UserID=Tester  
결과 예시 : 
```json
{
	"items": [
		{
			"Contents": "None",
			"Photo1": "",
			"Photo2": "",
			"Photo3": "",
			"Title": "test입니다.",
			"Town": "",
			"UploadTime": "2023-04-10 20:57:04",
			"UserID": "Tester",
			"WritingID": "2023-04-10 20:57:04"
		}
	],
	"total": 1
}
```

### 닉네임 변경
호출 URL : http://3.130.31.88:5000/MyPage/AKA?UserID=Tester&AKA=teste_AKA  
결과 예시 : sucess

### 동네 변경
호출 URL : http://3.130.31.88:5000/MyPage/Town?UserID=Tester&Town=%EC%88%98%EC%9B%90%EC%8B%9C%20%EC%98%81%ED%86%B5%EA%B5%AC%20%EC%9A%B0%EB%A7%8C%EB%8F%99   
결과 예시 : sucess

## 북마커
### 북마커 추가
호출 URL  : http://3.130.31.88:5000/Bookmark/add?StoreID=5064&StoreType=1&UserID=Tester  
결과 예시 : sucess

### 북마커 삭제
호출 URL  : http://3.130.31.88:5000/Bookmark/del?StoreID=5064&StoreType=1&UserID=Tester  
결과 예시 : sucess

### 북마커 조회
호출 URL : http://3.130.31.88:5000/Bookmark/list?UserID=Tester  
결과 예시 :
```json
{
	"items": [
		{
			"CateName": "식음료",
			"StoreID": 5063,
			"StoreName": "월드전&막걸리",
			"StorePhoto": "",
			"StorePointLat": 37.2795568,
			"StorePointLng": 127.0312058,
			"StoreType": "1",
			"SubCateName": "기타"
		},
		{
			"CateName": "식음료",
			"StoreID": 5064,
			"StoreName": "엉클돈까스",
			"StorePhoto": "",
			"StorePointLat": 37.27883002,
			"StorePointLng": 127.0435057,
			"StoreType": "1",
			"SubCateName": "기타"
		}
	],
	"total": 2
}
```


## 로그인
### 로그인 계정 추가
호출 URL : http://3.130.31.88:5000/LogIn/?Town=%EC%88%98%EC%9B%90%EC%8B%9C%20%EC%98%81%ED%86%B5%EA%B5%AC%20%EC%9B%90%EC%B2%9C%EB%8F%99&AKA=aka&userType=1&Card=9491111711112222&Profile&Account=ImTester  
결과 예시 : success