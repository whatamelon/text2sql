def update_ddl_context():
    # DB에서 최신 DDL 정보 가져오기
    ddl_info = db.get_table_info()
    
    # 테이블/컬럼 주석 정보 추가
    comments = get_table_comments()  # 별도 구현 필요
    
    return ddl_info + "\n" + comments