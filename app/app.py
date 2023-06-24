@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        #check if the credentials are valid
        if valid_credentials(username,password):
            session['username'] = username
            return redirect(url_for('insurance'))
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/insurance')
def insurance():
    #check if the user is logged in
    if 'username' in session:
        username = session['username']
        #render the insurance page
        return render_template('insurance.html', username=username)
    else:
        return redirect(url_for('login'))