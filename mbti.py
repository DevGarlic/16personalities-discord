import requests
from bs4 import BeautifulSoup
from lxml import html
import pandas as pd

def get_relationship(a,b):
    relationship = [
        ['', 'INFP', 'ENFP', 'INFJ', 'ENFJ', 'INTJ', 'ENTJ', 'INTP', 'ENTP', 'ISFP', 'ESFP', 'ISTP', 'ESTP', 'ISFJ', 'ESFJ', 'ISTJ', 'ESTJ'],
        ['INFP', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자'],
        ['ENFP', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자'],
        ['INFJ', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자'],
        ['ENFJ', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자'],
        ['INTJ', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님'],
        ['ENTJ', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!'],
        ['INTP', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '니 맘이 내 맘! 천생연분'],
        ['ENTP', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님'],
        ['ISFP', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분'],
        ['ESFP', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!'],
        ['ISTP', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분'],
        ['ESTP', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!'],
        ['ISFJ', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!'],
        ['ESFJ', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!'],
        ['ISTJ', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '최악은 아니지만, 좋은것도 아님', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!'],
        ['ESTJ', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '궁합 최악! 다시 생각해보자', '최악은 아니지만, 좋은것도 아님', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '최악은 아니지만, 좋은것도 아님', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '니 맘이 내 맘! 천생연분', '안 맞는 부분도 있지만, 맞는 부분도 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!', '아주 좋은 관계가 될 수 있음!']
    ]
    columns = relationship[0]
    data = relationship[1:]
    df = pd.DataFrame(data, columns=columns)
    df.set_index('', inplace=True)
    try:
        return df.loc[a.upper(), b.upper()]
    except KeyError:
        return "존재하지 않는 유형"

def get_test(a):
    test = ["주기적으로 새로운 친구를 만든다.","자유 시간 중 상당 부분을 다양한 관심사를 탐구하는 데 할애한다.","다른 사람이 울고 있는 모습을 보면 자신도 울고 싶어질 때가 많다.","일이 잘못될 때를 대비해 여러 대비책을 세우는 편이다.","압박감이 심한 환경에서도 평정심을 유지하는 편이다.","파티나 행사에서 새로운 사람에게 먼저 자신을 소개하기보다는 주로 이미 알고 있는 사람과 대화하는 편이다.","하나의 프로젝트를 완전히 완료한 후 다른 프로젝트를 시작하는 편이다.","매우 감상적인 편이다.","일정이나 목록으로 계획을 세우는 일을 좋아한다.","작은 실수로도 자신의 능력이나 지식을 의심하곤 한다.","관심이 가는 사람에게 다가가서 대화를 시작하기가 어렵지 않다.","예술 작품의 다양한 해석에 대해 토론하는 일에는 크게 관심이 없다.","감정보다는 이성을 따르는 편이다.","하루 일정을 계획하기보다는 즉흥적으로 하고 싶은 일을 하는 것을 좋아한다.","다른 사람에게 자신이 어떤 사람으로 보일지 걱정하지 않는 편이다.","단체 활동에 참여하는 일을 즐긴다.","결말을 자신의 방식으로 해석할 수 있는 책과 영화를 좋아한다.","자신보다는 남의 성공을 돕는 일에서 더 큰 만족감을 느낀다.","관심사가 너무 많아 다음에 어떤 일을 해야 할지 모를 때가 있다.","일이 잘못될까봐 자주 걱정하는 편이다.","단체에서 지도자 역할을 맡는 일은 가능한 피하고 싶다.","자신에게 예술적 성향이 거의 없다고 생각한다.","사람들이 감정보다는 이성을 중시했다면 더 나은 세상이 되었으리라고 생각한다.","휴식을 취하기 전에 집안일을 먼저 끝내기를 원한다.","다른 사람의 논쟁을 바라보는 일이 즐겁다.","다른 사람의 주의를 끌지 않으려고 하는 편이다.","감정이 매우 빠르게 변하곤 한다.","자신만큼 효율적이지 못한 사람을 보면 짜증이 난다.","해야 할 일을 마지막까지 미룰 때가 많다.","사후세계에 대한 질문이 흥미롭다고 생각한다.","혼자보다는 다른 사람과 시간을 보내고 싶어한다.","이론 중심의 토론에는 관심이 없으며 원론적인 이야기는 지루하다고 생각한다.","자신과 배경이 완전히 다른 사람에게도 쉽게 공감할 수 있다.","결정을 내리는 일을 마지막까지 미루는 편이다.","이미 내린 결정에 대해서는 다시 생각하지 않는 편이다.","혼자만의 시간을 보내기보다는 즐거운 파티와 행사로 일주일의 피로를 푸는 편이다.","미술관에 가는 일을 좋아한다.","다른 사람의 감정을 이해하기 힘들 때가 많다.","매일 할 일을 계획하는 일을 좋아한다.","불안함을 느낄 때가 거의 없다.","전화 통화를 거는 일은 가능한 피하고 싶다.","자신의 의견과 매우 다른 의견을 이해하기 위해 많은 시간을 할애하곤 한다.","친구에게 먼저 만나자고 연락하는 편이다.","계획에 차질이 생기면 최대한 빨리 계획으로 돌아가기 위해 노력한다.","오래전의 실수를 후회할 때가 많다.","인간의 존재와 삶의 이유에 대해 깊이 생각하지 않는 편이다.","감정을 조절하기보다는 감정에 휘둘리는 편이다.","상대방의 잘못이라는 것이 명백할 때도 상대방의 체면을 살려주기 위해 노력한다.","계획에 따라 일관성 있게 업무를 진행하기보다는 즉흥적인 에너지로 업무를 몰아서 처리하는 편이다.","상대방이 자신을 높게 평가하면 나중에 상대방이 실망하게 될까 걱정하곤 한다.","대부분의 시간을 혼자서 일할 수 있는 직업을 원한다.","철학적인 질문에 대해 깊게 생각하는 일은 시간 낭비라고 생각한다.","조용하고 사적인 장소보다는 사람들로 붐비고 떠들썩한 장소를 좋아한다.","상대방의 감정을 바로 알아차릴 수 있다.","무엇인가에 압도당하는 기분을 느낄 때가 많다.","단계를 건너뛰는 일 없이 절차대로 일을 완수하는 편이다.","논란이 되거나 논쟁을 불러일으킬 수 있는 주제에 관심이 많다.","자신보다 다른 사람에게 더 필요한 기회라고 생각되면 기회를 포기할 수도 있다.","마감 기한을 지키기가 힘들다.","일이 원하는 대로 진행될 것이라는 자신감이 있다."]
    try:
        return test[a]
    except:
        return "범위 초과 (0~59)"
    
def get_info(a):
    try:
        soup = BeautifulSoup(requests.get(f"https://www.16personalities.com/ko/%EC%84%B1%EA%B2%A9%EC%9C%A0%ED%98%95-{a}").text,'html.parser')
        nickname = soup.select_one('#main-app > main > header > div > h1 > span').get_text()
        description = html.fromstring(str(soup)).xpath('//*[@id="main-app"]/main/div[1]/div/article/p[1]/text()')[0]
        return {"mbti": a.upper(),"nickname":nickname,"description":description,"avatar":get_avatar(a.upper())}
    except:
        return "존재하지 않는 mbti 혹은 알 수 없는 오류"

def get_avatar(a):
    json = {"ENFJ": "https://i.ibb.co/6FKKSC6/enfj.png","ENFP": "https://i.ibb.co/Xt6yZSJ/enfp.png","ENTJ": "https://i.ibb.co/wgnJgJj/entj.png","ENTP": "https://i.ibb.co/ZcwjtH6/entp.png","ESFJ": "https://i.ibb.co/kSBVPQ5/esfj.png","ESFP": "https://i.ibb.co/4JTJDg7/esfp.png","ESTJ": "https://i.ibb.co/gDvLWP3/estj.png","ESTP": "https://i.ibb.co/jbSKMdq/estp.png","INFJ": "https://i.ibb.co/GtssndN/infj.png","INFP": "https://i.ibb.co/q9WKtYW/infp.png","INTJ": "https://i.ibb.co/Y7R0fk8/intj.png","INTP": "https://i.ibb.co/XDx9Gn7/intp.png","ISFJ": "https://i.ibb.co/GcN6RG9/isfj.png","ISFP": "https://i.ibb.co/hsKLgVf/isfp.png","ISTJ": "https://i.ibb.co/bH0q8vb/istj.png","ISTP": "https://i.ibb.co/DR1372g/istp.png"}
    if a in json:
        return json[a]
    else:
        return "존재하지 않는 유형"

def get_result(q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20, q21, q22, q23, q24, q25, q26, q27, q28, q29, q30, q31, q32, q33, q34, q35, q36, q37, q38, q39, q40, q41, q42, q43, q44, q45, q46, q47, q48, q49, q50, q51, q52, q53, q54, q55, q56, q57, q58, q59, q60):
    json = {
        "questions":[
            {
                "text":"주기적으로 새로운 친구를 만든다.",
                "answer": q1
            },
            {
                "text":"자유 시간 중 상당 부분을 다양한 관심사를 탐구하는 데 할애한다.",
                "answer": q2
            },
            {
                "text":"다른 사람이 울고 있는 모습을 보면 자신도 울고 싶어질 때가 많다.",
                "answer": q3
            },
            {
                "text":"일이 잘못될 때를 대비해 여러 대비책을 세우는 편이다.",
                "answer": q4
            },
            {
                "text":"압박감이 심한 환경에서도 평정심을 유지하는 편이다.",
                "answer": q5
            },
            {
                "text":"파티나 행사에서 새로운 사람에게 먼저 자신을 소개하기보다는 주로 이미 알고 있는 사람과 대화하는 편이다.",
                "answer": q6
            },
            {
                "text":"하나의 프로젝트를 완전히 완료한 후 다른 프로젝트를 시작하는 편이다.",
                "answer": q7
            },
            {
                "text":"매우 감상적인 편이다.",
                "answer": q8
            },
            {
                "text":"일정이나 목록으로 계획을 세우는 일을 좋아한다.",
                "answer": q9
            },
            {
                "text":"작은 실수로도 자신의 능력이나 지식을 의심하곤 한다.",
                "answer": q10
            },
            {
                "text":"관심이 가는 사람에게 다가가서 대화를 시작하기가 어렵지 않다.",
                "answer": q11
            },
            {
                "text":"예술 작품의 다양한 해석에 대해 토론하는 일에는 크게 관심이 없다.",
                "answer": q12
            },
            {
                "text":"감정보다는 이성을 따르는 편이다.",
                "answer": q13
            },
            {
                "text":"하루 일정을 계획하기보다는 즉흥적으로 하고 싶은 일을 하는 것을 좋아한다.",
                "answer": q14
            },
            {
                "text":"다른 사람에게 자신이 어떤 사람으로 보일지 걱정하지 않는 편이다.",
                "answer": q15
            },
            {
                "text":"단체 활동에 참여하는 일을 즐긴다.",
                "answer": q16
            },
            {
                "text":"결말을 자신의 방식으로 해석할 수 있는 책과 영화를 좋아한다.",
                "answer": q17
            },
            {
                "text":"자신보다는 남의 성공을 돕는 일에서 더 큰 만족감을 느낀다.",
                "answer": q18
            },
            {
                "text":"관심사가 너무 많아 다음에 어떤 일을 해야 할지 모를 때가 있다.",
                "answer": q19
            },
            {
                "text":"일이 잘못될까봐 자주 걱정하는 편이다.",
                "answer": q20
            },
            {
                "text":"단체에서 지도자 역할을 맡는 일은 가능한 피하고 싶다.",
                "answer": q21
            },
            {
                "text":"자신에게 예술적 성향이 거의 없다고 생각한다.",
                "answer": q22
            },
            {
                "text":"사람들이 감정보다는 이성을 중시했다면 더 나은 세상이 되었으리라고 생각한다.",
                "answer": q23
            },
            {
                "text":"휴식을 취하기 전에 집안일을 먼저 끝내기를 원한다.",
                "answer": q24
            },
            {
                "text":"다른 사람의 논쟁을 바라보는 일이 즐겁다.",
                "answer": q25
            },
            {
                "text":"다른 사람의 주의를 끌지 않으려고 하는 편이다.",
                "answer": q26
            },
            {
                "text":"감정이 매우 빠르게 변하곤 한다.",
                "answer": q27
            },
            {
                "text":"자신만큼 효율적이지 못한 사람을 보면 짜증이 난다.",
                "answer": q28
            },
            {
                "text":"해야 할 일을 마지막까지 미룰 때가 많다.",
                "answer": q29
            },
            {
                "text":"사후세계에 대한 질문이 흥미롭다고 생각한다.",
                "answer": q30
            },
            {
                "text":"혼자보다는 다른 사람과 시간을 보내고 싶어한다.",
                "answer": q31
            },
            {
                "text":"이론 중심의 토론에는 관심이 없으며 원론적인 이야기는 지루하다고 생각한다.",
                "answer": q32
            },
            {
                "text":"자신과 배경이 완전히 다른 사람에게도 쉽게 공감할 수 있다.",
                "answer": q33
            },
            {
                "text":"결정을 내리는 일을 마지막까지 미루는 편이다.",
                "answer": q34
            },
            {
                "text":"이미 내린 결정에 대해서는 다시 생각하지 않는 편이다.",
                "answer": q35
            },
            {
                "text":"혼자만의 시간을 보내기보다는 즐거운 파티와 행사로 일주일의 피로를 푸는 편이다.",
                "answer": q36
            },
            {
                "text":"미술관에 가는 일을 좋아한다.",
                "answer": q37
            },
            {
                "text":"다른 사람의 감정을 이해하기 힘들 때가 많다.",
                "answer": q38
            },
            {
                "text":"매일 할 일을 계획하는 일을 좋아한다.",
                "answer": q39
            },
            {
                "text":"불안함을 느낄 때가 거의 없다.",
                "answer": q40
            },
            {
                "text":"전화 통화를 거는 일은 가능한 피하고 싶다.",
                "answer": q41
            },
            {
                "text":"자신의 의견과 매우 다른 의견을 이해하기 위해 많은 시간을 할애하곤 한다.",
                "answer": q42
            },
            {
                "text":"친구에게 먼저 만나자고 연락하는 편이다.",
                "answer": q43
            },
            {
                "text":"계획에 차질이 생기면 최대한 빨리 계획으로 돌아가기 위해 노력한다.",
                "answer": q44
            },
            {
                "text":"오래전의 실수를 후회할 때가 많다.",
                "answer": q45
            },
            {
                "text":"인간의 존재와 삶의 이유에 대해 깊이 생각하지 않는 편이다.",
                "answer": q46
            },
            {
                "text":"감정을 조절하기보다는 감정에 휘둘리는 편이다.",
                "answer": q47
            },
            {
                "text":"상대방의 잘못이라는 것이 명백할 때도 상대방의 체면을 살려주기 위해 노력한다.",
                "answer": q48
            },
            {
                "text":"계획에 따라 일관성 있게 업무를 진행하기보다는 즉흥적인 에너지로 업무를 몰아서 처리하는 편이다.",
                "answer": q49
            },
            {
                "text":"상대방이 자신을 높게 평가하면 나중에 상대방이 실망하게 될까 걱정하곤 한다.",
                "answer": q50
            },
            {
                "text":"대부분의 시간을 혼자서 일할 수 있는 직업을 원한다.",
                "answer": q51
            },
            {
                "text":"철학적인 질문에 대해 깊게 생각하는 일은 시간 낭비라고 생각한다.",
                "answer": q52
            },
            {
                "text":"조용하고 사적인 장소보다는 사람들로 붐비고 떠들썩한 장소를 좋아한다.",
                "answer": q53
            },
            {
                "text":"상대방의 감정을 바로 알아차릴 수 있다.",
                "answer": q54
            },
            {
                "text":"무엇인가에 압도당하는 기분을 느낄 때가 많다.",
                "answer": q55
            },
            {
                "text":"단계를 건너뛰는 일 없이 절차대로 일을 완수하는 편이다.",
                "answer": q56
            },
            {
                "text":"논란이 되거나 논쟁을 불러일으킬 수 있는 주제에 관심이 많다.",
                "answer": q57
            },
            {
                "text":"자신보다 다른 사람에게 더 필요한 기회라고 생각되면 기회를 포기할 수도 있다.",
                "answer": q58
            },
            {
                "text":"마감 기한을 지키기가 힘들다.",
                "answer": q59
            },
            {
                "text":"일이 원하는 대로 진행될 것이라는 자신감이 있다.",
                "answer": q60
            }
        ],
        "gender":"",
        "inviteCode":"",
        "teamInviteKey":"",
        "extraData":[]
    }
    result = requests.post("https://www.16personalities.com/ko/%EA%B2%80%EC%82%AC-%EA%B2%B0%EA%B3%BC-%EB%B3%B4%EA%B8%B0",json=json)
    session = requests.get("https://www.16personalities.com/api/session",cookies=result.cookies).json()
    soup = BeautifulSoup(requests.get(result.json()['redirect']).text,'html.parser')
    nickname = soup.select_one('#main-app > main > header > div > h1 > span').get_text()
    description = html.fromstring(str(soup)).xpath('//*[@id="main-app"]/main/div[1]/div/article/p[1]/text()')[0]
    mbti = session['user']['publicUrl'].split("/")[4].upper()
    url = f"https://www.16personalities.com/ko/%EA%B2%B0%EA%B3%BC/{mbti.lower()}/x/{session['user']['publicUrl'].split('/')[6]}"
    return {"mbti": mbti,"nickname":nickname,"description":description,"url":url,"avatar":get_avatar(mbti.split("-")[0])}