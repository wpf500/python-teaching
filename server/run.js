var express = require('express');
var bodyParser = require('body-parser');
var spawn = require('child_process').spawn;

var app = express();

app.use(bodyParser.text());
app.use(express.static('.'));

app.post('/run', function (req, res) {
    var body = req.body;

    var proc = spawn('python');
    var output = '';
    proc.stdout.on('data', function (data) { output += data; });
    proc.stderr.on('data', function (data) { output += data; });

    proc.on('close', function () {
        res.header('Content-Type', 'text/plain');
        res.send(output);
    });

    proc.stdin.write(body);
    proc.stdin.end();
});

app.listen(3000, function () {
    console.log('Listening on 3000');
});
