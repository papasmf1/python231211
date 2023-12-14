import requests
from bs4 import BeautifulSoup

def naver_blog_crawler(search_keyword):
    # 검색어로 블로그 검색 결과 페이지 URL 생성
    base_url = "https://search.naver.com/search.naver"
    params = {
        "where": "post",
        "sm": "tab_jum",
        "query": search_keyword,
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 블로그 검색 결과를 가져오기
        blog_results = soup.find_all("li", class_="sh_blog_top")
        
        for result in blog_results:
            # 블로그명 추출
            blog_name = result.find("a", class_="sh_blog_title").text
            
            # 블로그 주소 추출
            blog_url = result.find("a", class_="sh_blog_title")["href"]
            
            # 제목 추출
            title = result.find("a", class_="sh_blog_title").attrs.get("title", "")
            
            # 포스팅 날짜 추출
            post_date = result.find("span", class_="date").text
            
            # 결과 출력
            print("블로그명:", blog_name)
            print("블로그 주소:", blog_url)
            print("제목:", title)
            print("포스팅 날짜:", post_date)
            print("\n")
    else:
        print("HTTP 요청 오류:", response.status_code)

if __name__ == "__main__":
    search_keyword = input("검색어를 입력하세요: ")
    naver_blog_crawler(search_keyword)
