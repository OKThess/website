<?php
 if (isset($_POST["submit"])) {
      $name = htmlspecialchars($_POST['name'], ENT_QUOTES, 'UTF-8');
      $email = htmlspecialchars($_POST['email'], ENT_QUOTES, 'UTF-8');
      $phone = htmlspecialchars($_POST['phone'], ENT_QUOTES, 'UTF-8');
      $message1 = htmlspecialchars($_POST['message1'], ENT_QUOTES, 'UTF-8');
      $message2 = htmlspecialchars($_POST['message2'], ENT_QUOTES, 'UTF-8');
      $message3 = htmlspecialchars($_POST['message3'], ENT_QUOTES, 'UTF-8');
      $message4 = htmlspecialchars($_POST['message4'], ENT_QUOTES, 'UTF-8');
      $human = intval($_POST['human']);
      $from = 'From: OK!THESS Application Form <apply@okthess.gr>';
      $to = 'apply@okthess.gr';
      $subject = '=?UTF-8?B?' . base64_encode('Νέα αίτηση συμμετοχής') . '?=';

      $body = "From: $name\n E-Mail: $email\n Answer-1: $message1\n Answer-2: $message2\n Answer-3: $message3\n Answer-4: $message4";
      if (!$_POST['name']) {
          $errName = 'Fill in your full name';
      }
      if (!$_POST['email'] || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
          $errEmail = 'The e-mail address is not valid';
      }
      if (!$_POST['phone']) {
          $errPhone = 'Fill in your phone number';
      }
      if (!$_POST['message1']) {
          $errMessage1 = 'Required answer';
      }
      if (!$_POST['message2']) {
          $errMessage2 = 'Required answer';
      }
      if (!$_POST['message3']) {
          $errMessage3 = 'Required answer';
      }
      if (!$_POST['message4']) {
          $errMessage4 = 'Required answer';
      }
      if ($human !== 5) {
          $errHuman = 'Your answer is wrong';
      }
      if (!$errName && !$errEmail && !$errMessage1 && !$errHuman) {
          if (mail($to, $subject, $body, $from)) {
            $result = '<div class="alert alert-success">We have just received your e-mail. You will be further informed about your submission upon the evaluation process completion.</div>';
          } else {
            $result = '<div class="alert alert-danger">Oups!Something went terribly wrong, please try again</div>';
      }
     }
    }
?>
<!DOCTYPE html>
<html lang="en" itemscope itemtype="https://schema.org/ProfessionalService">
<head>
  <meta charset="utf-8"/>
  <meta http-equiv="encoding" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <title>OK!Thess | Application Form</title>
  <meta http-equiv="Content-Type" content="text/html">
  <meta name="description" content="We accept at any time submissions from individuals or groups with innovative ideas, regardless their stage, who would like to benefit from the services of the OK!Thess pre-incubator">
  <meta name="robots" content="NOODP">
  <meta name="author" content="ntemposd">

  <meta itemprop="name" content="OK!Thess">
  <meta itemprop="description" content="We accept at any time submissions from individuals or groups with innovative ideas, regardless their stage, who would like to benefit from the services of the OK!Thess pre-incubator">
  <meta itemprop="image" content="/img/thumb.png">

  <meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@okthess">
	<meta name="twitter:creator" content="@ntemposd">
	<meta name="twitter:title" content="OK!Thess">
	<meta name="twitter:description" content="We accept at any time submissions from individuals or groups with innovative ideas, regardless their stage, who would like to benefit from the services of the OK!Thess pre-incubator">
	<meta name="twitter:image" content="http://www.okthess.gr/img/thumb.png">

  <meta property="og:title" content="OK!Thess">
  <meta property="og:description" content="We accept at any time submissions from individuals or groups with innovative ideas, regardless their stage, who would like to benefit from the services of the OK!Thess pre-incubator">
  <meta property="og:url" content="http://okthess.gr">
  <meta property="og:image" content="/img/thumb.png">
  <meta property="og:type" content="website">

  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="/style/main.css">
  <link rel="stylesheet" type="text/css" href="/style/app.css">
  <link href="https://fonts.googleapis.com/css?family=Roboto:100,300,400,500,700&amp;subset=greek,greek-ext" rel="stylesheet">
  <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
    ga('create', 'UA-49294327-5', 'auto');
    ga('send', 'pageview');
  </script>
</head>
<body>
<nav class="navbar navbar-default container-fluid">
	<div class="navbar-header">
		<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse" aria-expanded="false">
     <span class="icon-bar"></span>
     <span class="icon-bar"></span>
		 <span class="icon-bar"></span>
		</button>
		<a class="navbar-brand" href="/eng/index.html"><img src="/img/logo.png" alt="Logo"></a>
	</div>
	 <div class="collapse navbar-collapse" id="navbar-collapse">
		<ul class="nav navbar-nav navbar-right">
			<li class="dropdown">
				<a class="dropdown-toggle" data-toggle="dropdown" href="#">About <b class="caret"></b></a>
  				<ul class="dropdown-menu">
    				<li><a tabindex="-1" href="/eng/about.html#collapse0">What we do</a></li>
    				<li><a tabindex="-1" href="/eng/about.html#collapse1">How do we do it?</a></li>
    				<li><a tabindex="-1" href="/eng/about.html#collapse2">How do I participate?</a></li>
						<li><a tabindex="-1" href="/eng/about.html#collapse3">Coworking space</a></li>
      		</ul>
			</li>
			<li><a href="/eng/teams.html">Hosted teams</a></li>
      <li><a href="/eng/news.html">News</a></li>
      <li><a href="/eng/knowledge-base.html">Knowledge base</a></li>
			<li><a href="/eng/app.php">To join</a></li>
			<li><a href="/eng/hi.php">Contact</a></li>
      <li><a href="/eng/under-construction.html">Members</a></li>
		</ul>
	</div>
</nav>
<span id="lang"><a href="http://okthess.gr/app.php">GR</a></span>
<section class="jumbotron">
 <div class="container">
   <h1>Application Form</h1>
   <p>General information and online application form, for the OK!Thess pre-incubation program.</p>
 </div>
</section>
<div class="container">
  <p>We accept at any time submissions from individuals or groups with innovative ideas, regardless their stage, who would like to benefit from the services of the OK!Thess pre-incubator in order to set up a startup business or accelarate the one that they already have set up.</p>
  <p>Proposals shall be evaluated at regular intervals, the exact dates are being announced on this website. The last assessment period closed on December the 1st, 2016 while the next one is scheduled for early 2017. The exact date will be announced in the near future.</p>
  <p>To participate, you either fill in the following form, or just answer the questions in the body of an e-mail and send it to <strong><small>apply@okthess.gr</small></strong></p>
  <br>
  <a class="btn btn-primary" href="http://okthess.gr/pdf/website-open-call.pdf" role="button" target="_blank">Information<small> - GR</small></a>
  <a class="btn btn-primary" href="http://okthess.gr/under-construction.html" role="button" target="_blank">Internal regulation</a>
  <br>
  <br>
  <h2 class="text-muted">Application Form</h2>
  ---------------
  <form class="form-horizontal" role="form" method="post" action="app.php">
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message1" placeholder="What is the business idea that you want to deploy the OK!Thess (up to 150 words)?"><?php echo htmlspecialchars($_POST['message1']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage1</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message2" placeholder="Which is your target market (where do you see your prospective customers) (up to 100 words)?"><?php echo htmlspecialchars($_POST['message2']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage2</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message3" placeholder="Do you know your product's/service's competitors (up to 100 words)?"><?php echo htmlspecialchars($_POST['message3']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage3</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message4" placeholder="What do you expect to get form OK!Thess, except space and infrastructure (up to 100 words)?"><?php echo htmlspecialchars($_POST['message4']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage4</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="text" class="form-control" id="phone" name="phone" placeholder="Contact phone" value="<?php echo htmlspecialchars($_POST['phone']); ?>">
          <?php echo "<p class='text-danger'>$errPhone</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="email" class="form-control" id="email" name="email" placeholder="Contact e-mail" value="<?php echo htmlspecialchars($_POST['email']); ?>">
          <?php echo "<p class='text-danger'>$errEmail</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="text" class="form-control" id="name" name="name" placeholder="Full name" value="<?php echo htmlspecialchars($_POST['name']); ?>">
          <?php echo "<p class='text-danger'>$errName</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="number" class="form-control" id="human" name="human" placeholder="Result of (2 + 3 = ?)">
          <?php echo "<p class='text-danger'>$errHuman</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input id="submit" name="submit" type="submit" value="Submit" class="btn btn-primary">
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <?php echo $result; ?>
      </div>
    </div>
  </form>
</div>
<footer class="site-footer">
	<div class="container">
		<div class="row" id="social">
			<a href="mailto:mail@okthess.gr" target="_blank"><img social src="/img/email.png" alt="email"></a>
			<a href="https://www.facebook.com/OKThess/" target="_blank"><img social src="/img/facebook.png" alt="facebook"></a>
			<a href="https://twitter.com/okthess" target="_blank"><img social src="/img/twitter.png" alt="twitter"></a>
		</div>
		<div class="row">
			<div class="col-md-4 col-sm-4">
				<h5>LOCATION</h5>
				<hr>
					<div id="map-outer">
						<div id="map-container"></div>
						<script src="/js/map.js"></script>
					</div>
			</div>
			<div class="col-md-4 col-sm-4">
				<h5>MEMBERS</h5><hr>
				<a href="https://www.auth.gr/en" target="_blank"><img src="/eng/img/AUTH.png" alt="Aristotle_University_Thessaloniki"></a>
				<a href="http://www.thessaloniki.gr/portal/page/portal/EnglishPage" target="_blank"><img src="/eng/img/municipality.jpg" alt="Municipality_of_Thessaloniki"></a>
				<a href="http://www.uom.gr/index.php?newlang=eng" target="_blank"><img src="/img/UOM.png" alt="University_Of_Macedonia"></a>
				<a href="http://www.thessinnozone.gr/en/" target="_blank"><img src="/eng/img/TIZ.jpg" alt="Thessaloniki_Innovation_Zone"></a>
				<a href="http://www.ihu.edu.gr/" target="_blank"><img src="/eng/img/IHU.jpg" alt="International_Hellenic_University"></a>
				<a href="http://www.teithe.gr/index_en.html" target="_blank"><img src="/img/ATEITH.jpg" alt="Alexander_Technological_Institute_Thessaloniki"></a>
				<a href="http://en.sbbe.gr/" target="_blank"><img src="/eng/img/SBBE.jpg" alt="SBBE"></a>
				<a href="http://www.seve.gr/en/" target="_blank"><img src="/eng/img/SEVE.jpg" alt="SEVE"></a>
			</div>
			<div class="col-md-4 col-sm-4">
				<h5>SPONSORS</h5><hr>
				<a href="http://www.hcn.gr/" target="_blank"><img src="/img/hcn.jpg" alt="HCN"></a>
				<a href="http://www.beetroot.gr/" target="_blank"><img src="/img/beetroot.png" alt="Beetroot"></a>
				<a href="https://www.ast.gr/en/" target="_blank"><img src="/img/ast.png" alt="AST"></a>
				<h5>DONOR</h5><hr>
				<a href="http://www.snf.org/en/" target="_blank"><img src="/img/ISN.jpg" alt="ISN"></a>
			</div>
		</div>
	</div>
		<p id="copy">Lovingly crafted by <a href="http://ntemposd.me" target="_blank">ntemposd</a></p>
</footer>
<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyB7E2raajPS5-4vEpx-LBOV0XkItvWQRt8&signed_in=true&callback=initMap"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
</body>
</html>
