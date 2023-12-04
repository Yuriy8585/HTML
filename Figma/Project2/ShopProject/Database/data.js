
const express = require('express');
const Visit = require('./database');

const app = express();
app.use(express.json());

app.post('/visit', async (req, res) => {
  const { ip, name, email } = req.body;

  try {
    const visit = new Visit({
      ip,
      name,
      email
    });
    await visit.save();

    res.sendStatus(200);
  } catch (error) {
    console.error(error);
    res.sendStatus(500);
  }
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});


/*

db = openDatabase("ToDo", "0.1", "A list of to do items.", 200000);
    if(!db){alert("Failed to connect to database.");}

db.transaction(function(tx) {
        tx.executeSql("SELECT COUNT(*) FROM ToDo", [], function (result) { alert('dsfsdf') }, function (tx, error) {
        tx.executeSql("CREATE TABLE ToDo (id REAL UNIQUE, label TEXT, timestamp REAL)", [], null, null);
        })});

db.transaction(function(tx) {
            tx.executeSql("INSERT INTO ToDo (label, timestamp) values(?, ?)", ["Купить iPad или HP Slate", new Date().getTime()], null, null);
            });

db.transaction(function(tx) {
                tx.executeSql("SELECT * FROM ToDo", [], function(tx, result) {
                for(var i = 0; i < result.rows.length; i++) {
                document.write('<b>' + result.rows.item(i)['label'] + '</b><br />');
                }}, null)});
                */