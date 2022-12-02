import express from 'express';
import http from 'http';

// Démarre Express
const app = express();
app.set('view engine', 'pug');
app.set('views', 'views/');

// Démarre le serveur
const server = http.createServer(app);
server.listen(3000, () => {
  console.log('Serveur démarré');
});

let messages = [];
let styles = {'background': 'white', "color": "black"};

app.get('/', (req, res) => {
  res.render('index', {messages, styles});
  res.end();
});

app.get('/message', (req, res) => {
  const {text} = req.query;
  messages.push({text});
  res.sendStatus(200);
});

app.get('/background', (req, res) => {
  const {background} = req.query;
  styles['background'] = background;
  res.sendStatus(200);
});

app.get('/color', (req, res) => {
  const {color} = req.query;
  styles['color'] = color;
  res.sendStatus(200);
});

