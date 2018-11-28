const express = require('express')
const app = express()

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
app.listen(3000, () => {
	console.log('server is running at 3000')
})