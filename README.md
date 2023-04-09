# DreameAPI

접근 URL : http://3.130.31.88:5000

## 지도
### 마커 띄우기
호출 URL : POST http://3.130.31.88:5000/MyPosition?myPositionLng=127.043517&myPositionLat=37.28224800000001&mbr=5000  
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
호출 URL : POST http://3.130.31.88:5000/Choose/Category?Category=2&myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000  
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
호출 URL : POST http://3.130.31.88:5000/Choose/SubCategory?Category=2&SubCategory=2&myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000  
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
호출 URL : POST http://3.130.31.88:5000/Choose/StoreType?StoreType=1&myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000  
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
호출 URL : http://3.130.31.88:5000/KeywordSearch?myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000&Keyword=%EC%8A%A4%EC%8B%9C  
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
호출 URL : http://3.130.31.88:5000/StoreDetail?StoreID=5064&StoreType=1  
결과 예시 :  
```json
{
	"items": [
		{
			"Address": "경기도 수원시 팔달구 아주로 43-1",
			"CateName": "식음료",
			"DayFinish": "0:00:00",
			"DayStart": "0:00:00",
			"DetailAddress": "",
			"HoliFinish": "0:00:00",
			"HoliStart": "0:00:00",
			"Item": "",
			"Phone": "031-216-8579",
			"Provided1": "",
			"Provided2": "",
			"SatFinish": "0:00:00",
			"SatStart": "0:00:00",
			"StoreID": 5064,
			"StoreName": "엉클돈까스",
			"StorePhoto": "",
			"StoreType": "1",
			"SubCateName": "기타",
			"WorkDay": ""
		}
	],
	"total": 1
}
```


## 푸드쉐어링
### 글등록
호출 URL : http://3.130.31.88:5000/StoreDetail?StoreID=5064&StoreType=1  
결과예시 : sucess

### 글등록
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
			"UploadTime": "2023-04-09 12:33:31",
			"UserID": "Tester",
			"WritingID": "2023-04-09 12:33:31"
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
			"UploadTime": "2023-04-09 12:33:31",
			"UserID": "Tester",
			"WritingID": "2023-04-09 12:33:31"
		}
	],
	"total": 1
}
```

## 북마커
### 북마커 추가
호출 URL  : http://3.130.31.88:5000/Bookmark/add?StoreID=5064&StoreType=1&UserID=Tester  
결과 예시 : sucess