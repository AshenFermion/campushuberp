import asyncio
import uvicorn
from app.database.db import init_db
from app.services.async_service import load_all_data,generate_all_reports
from app.utils.serializers import export_data
from app.utils.concurrency import calculate_totals_with_process
from app.utils.logger import get_logger

def run_startup_tasks():
    init_db()
    print("Loading You, Faculty, Courses and Enrollments...")
    asyncio.run(load_all_data())
    print("All data loaded successfully. Generating reports...")
    asyncio.run(generate_all_reports())
    print("All reports generated successfully.")
    export_data()
    print("Record summary:",calculate_totals_with_process())
    get_logger().info("Startup tasks completed")

if __name__=="__main__":
    run_startup_tasks()
    uvicorn.run("app.main:app",host="127.0.0.1",port=8000,reload=False)
