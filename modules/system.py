import platform
import psutil

async def system_info(_):
    return {
        "system": platform.system(),
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent
    }
