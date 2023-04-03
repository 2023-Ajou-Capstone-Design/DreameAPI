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
호출 URL : POST http://3.130.31.88:5000/Category?Category=2&SubCategory=2&StoreType=1&myPositionLng=127.043517&myPositionLat=37.28224&mbr=5000
결과예시 : 
```json
{
	"items": [
		{
			"CateName": "마트",
			"Category": "2",
			"Distance": 4688.589533690853,
			"StoreID": 2561,
			"StoreName": "씨유수원세류3동점",
			"StorePhoto": "",
			"StorePointLat": 37.2492,
			"StorePointLng": 127.076,
			"StoreType": "1",
			"SubCateName": "편의점",
			"SubCategory": "2"
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