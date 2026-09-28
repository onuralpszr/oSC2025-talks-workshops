from smolagents import CodeAgent, LiteLLMModel, tool
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    insert,
    inspect,
    text,
)

model = LiteLLMModel(
    model_id="ollama_chat/llama3.1:8b-instruct-q8_0",
    api_base="http://localhost:11434",
    api_key="openSUSE-is-awesome",
    num_ctx=8192,
)


engine = create_engine("sqlite:///:memory:")
metadata_obj = MetaData()

# create city SQL table
table_name = "hackweek_projects"
receipts = Table(
    table_name,
    metadata_obj,
    Column("project_id", Integer, primary_key=True),
    Column("contributor_name", String(32), primary_key=True),
    Column("lines_of_code", Integer),
    Column("bugs_introduced", Integer),
)
metadata_obj.create_all(engine)

rows = [
    {
        "project_id": 1,
        "contributor_name": "Alan Payne",
        "lines_of_code": 1206,
        "bugs_introduced": 12,
    },
    {
        "project_id": 2,
        "contributor_name": "Alex Mason",
        "lines_of_code": 2386,
        "bugs_introduced": 24,
    },
    {
        "project_id": 3,
        "contributor_name": "Woodrow Wilson",
        "lines_of_code": 5343,
        "bugs_introduced": 54,
    },
    {
        "project_id": 4,
        "contributor_name": "Margaret James",
        "lines_of_code": 2111,
        "bugs_introduced": 10,
    },
]
for row in rows:
    stmt = insert(receipts).values(**row)
    with engine.begin() as connection:
        cursor = connection.execute(stmt)

inspector = inspect(engine)
columns_info = [(col["name"], col["type"]) for col in inspector.get_columns(table_name)]

table_description = "Columns:\n" + "\n".join(
    [f"  - {name}: {col_type}" for name, col_type in columns_info]
)
print(table_description)


@tool
def sql_engine(query: str) -> str:
    """
    Allows you to perform SQL queries on the table. Returns a string representation of the result.
    The table is named 'hackweek_projects'. Its description is as follows:
        Columns:
        - project_id: INTEGER
        - contributor_name: VARCHAR(32)
        - lines_of_code: INTEGER
        - bugs_introduced: INTEGER

    Args:
        query: The query to perform. This should be correct SQL.
    """
    output = ""
    with engine.connect() as con:
        rows = con.execute(text(query))
        for row in rows:
            output += "\n" + str(row)
    return output


agent = CodeAgent(tools=[sql_engine], model=model)
agent.run("Can you give me the name of the contributor with the most lines of code?")
