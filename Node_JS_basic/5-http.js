const http = require('http');
const countStudents = require('./3-read_file_async');

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    console.log('This is the list of our students');
    countStudents(process.argv[2])
      .then((m) => {
        res.end(`This is the list of our students\n${m}`);
      })
      .catch(() => {
        res.end('This is the list of our students\nCannot load the database');
      });
  } else {
    res.statusCode = 404;
  }
});
const app = server;
app.listen(1245, '127.0.0.1', () => {
  console.log('Server running at http://127.0.0.1:1245/');
});
module.exports = app;
