from apscheduler.schedulers.background import BackgroundScheduler
import parser
import time

def job():
    print("🚀 Запуск парсера...")
    parser.parse_sportsdirect()

if __name__ == "__main__":
    parser.init_db()

    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', hours=4)

    scheduler.start()
    print("✅ Планировщик запущен. Парсер будет выполняться каждые 4 часа.")

    try:
        while True:
            time.sleep(60)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
