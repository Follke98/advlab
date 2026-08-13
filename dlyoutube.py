
import yt_dlp


def download_youtube(url):
    options = {
        # ดาวน์โหลดคุณภาพดีที่สุดที่มี
        "format": "bestvideo+bestaudio/best",

        # ชื่อไฟล์ที่บันทึก
        "outtmpl": "%(title)s.%(ext)s",

        # ให้ yt-dlp ใช้ ffmpeg รวมเสียงและวิดีโอ
        "merge_output_format": "mp4",

        # แสดงความคืบหน้าการดาวน์โหลด
        "progress_hooks": [progress_hook],
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        print("\nดาวน์โหลดเสร็จเรียบร้อย!")

    except Exception as e:
        print(f"\nเกิดข้อผิดพลาด: {e}")


def progress_hook(data):
    if data["status"] == "downloading":
        percent = data.get("_percent_str", "0%")
        speed = data.get("_speed_str", "ไม่ทราบ")
        eta = data.get("_eta_str", "ไม่ทราบ")

        print(
            f"\rกำลังดาวน์โหลด: {percent} | "
            f"ความเร็ว: {speed} | "
            f"เหลือเวลา: {eta}",
            end=""
        )

    elif data["status"] == "finished":
        print("\nดาวน์โหลดไฟล์เสร็จ กำลังประมวลผล...")


if __name__ == "__main__":
    print("=== YouTube Downloader ===")

    url = input("กรุณาใส่ URL ของ YouTube: ")

    if url.strip():
        download_youtube(url)
    else:
        print("ไม่ได้ระบุ URL")
