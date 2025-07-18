from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {
        "input": "이번 달 매출이 얼마야?",
        "query": "SELECT SUM(amount) FROM sales WHERE DATE_TRUNC('month', created_at) = DATE_TRUNC('month', CURRENT_DATE)"
    },
    {
        "input": "가장 많이 팔린 상품 top 5는?",
        "query": "SELECT product_name, COUNT(*) as cnt FROM sales GROUP BY product_name ORDER BY cnt DESC LIMIT 5"
    }
]

example_prompt = PromptTemplate.from_template(
    "User input: {input}\nSQL query: {query}"
)

few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="당신은 SQL 전문가입니다. DDL과 테이블 설명을 참고하여 자연어 질문을 SQL로 변환하세요.\n\nDDL:\n{table_info}",
    suffix="User input: {input}\nSQL query:",
    input_variables=["input", "table_info"],
)