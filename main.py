def main():
    print("Hello from text2sql-project!")
    # 질문 처리
    question = "지난 주 신규 가입자 수는 몇 명이야?"
    result = agent.invoke({"input": question})

    # 결과를 자연어로 변환
    final_answer = llm.invoke(
        f"다음 SQL 쿼리 결과를 자연어로 설명해줘: {result}"
    )


if __name__ == "__main__":
    main()
