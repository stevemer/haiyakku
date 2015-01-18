
htmls = """\
<!DOCTYPE html>
<html>
<head>
	<title>Haiyakkus</title>

	<!-- jQuery Library -->
	 <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>

	<!-- Bootstrap Library -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>

	<!-- Font Awesome -->
	<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">

	<!-- Google Fonts -->
	<link href='http://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>

	<link rel="stylesheet" type="text/css" href="/static/styles.css">
	<script type="text/javascript" src="scripts.js"></script>

</head>

<body>
	<div class="jumbotron text-center">
		<div class="container">
			<h1>Welcome to Haiyakkus!</h1>
		</div>
	</div>
	<div class="container">
		<div class="row haiyakku">
			<span class="col-md-6 col-md-offset-2 haiyakku-text" >
				{0}<br>
				{1}<br>
				{2}<br>
			</span>
			<span class="col-md-2 haiyakku-vote">
				<i class="fa fa-chevron-up fa-lg"></i>
				<i class="fa fa-chevron-down fa-lg"></i>
			</span>
		</div>
	</div>
    <div id="refresh button">
        <button type="button" class="btn btn-primary" id="still-life-btn" onClick="window.location.reload()">More poetry!</button>
    
    </div>
</body>
</html>"""
