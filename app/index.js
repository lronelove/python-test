const express = require('express')
const app = express()
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false })

app.get('/', (req, res) => {
	const data = {
		code: 0,
		msg: "hello world"
	}
	res.send('hello world')
})
app.get('/home', (req, res) => {
	const data = {
		code: 0,
		msg: "hello world"
	}
	res.send(data)
})
app.post('/test', urlencodedParser, (req, res) => {
	const username = req.body.username || 0
	const password = req.body.password || 0

	res.send({
		username,
		password
	})
})
app.listen(3000, () => {
	console.log('server is running at 3000')
})