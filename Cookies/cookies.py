from flask import Flask, request, flash, url_for, redirect, render_template, make_response

# Cookies Demo
@app.route('/set', methods=['GET', 'POST'])
def setcookie():

	resp = make_response("Setting Cookie!")
	resp.set_cookie("webcast", "Cookie Tutorial")

    return resp


@app.route('/get', methods=['GET', 'POST'])
def getcookie():

	webcast = request.cookies.get('webcast')

	return "The webcasts is about {}".format(webcast)