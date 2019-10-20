const { spawn } = require('child_process');

const sensor = spawn('python', ['test/MainSender.py']);
sensor.stdout.on('data', function (data) {
    console.log(data.toString());
});