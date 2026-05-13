from flask import Flask, render_template, jsonify
import psutil
import datetime

app = Flask(__name__)

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    
    return {
        'cpu_percent': cpu,
        'memory_percent': memory.percent,
        'memory_used': round(memory.used / (1024**3), 2),
        'memory_total': round(memory.total / (1024**3), 2),
        'disk_percent': disk.percent,
        'disk_used': round(disk.used / (1024**3), 2),
        'disk_total': round(disk.total / (1024**3), 2),
        'net_sent': round(net.bytes_sent / (1024**2), 2),
        'net_recv': round(net.bytes_recv / (1024**2), 2),
        'timestamp': datetime.datetime.now().strftime('%H:%M:%S')
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/stats')
def stats():
    return jsonify(get_system_stats())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
