from collections import Counter

def analyze_logs(logs):

    failed_logins = 0
    successful_logins = 0
    unknown_events = 0

    failed_users = []
    recent_events = []

    for log in logs:

        log = log.strip()

        user = "Unknown"
        event_id = "Unknown"
        ip = "Unknown"
        status = "Unknown"

        # استخراج اسم المستخدم
        if "User:" in log:
            try:
                user = log.split("User:")[1].split("|")[0].strip()
            except:
                pass

        # استخراج Event ID
        if "EventID:" in log:
            try:
                event_id = log.split("EventID:")[1].split("|")[0].strip()
            except:
                pass

        # استخراج IP (إذا كان موجود)
        if "IP:" in log:
            try:
                ip = log.split("IP:")[1].strip()
            except:
                pass

        # تحليل الحدث
        if event_id == "4625":
            failed_logins += 1
            failed_users.append(user)
            status = "Failed Login"

        elif event_id == "4624":
            successful_logins += 1
            status = "Successful Login"

        else:
            unknown_events += 1
            status = "Unknown Event"

        recent_events.append({
            "user": user,
            "event_id": event_id,
            "ip": ip,
            "status": status
        })

    return {
        "failed_logins": failed_logins,
        "successful_logins": successful_logins,
        "unknown_events": unknown_events,
        "failed_users": Counter(failed_users),
        "recent_events": recent_events
    }