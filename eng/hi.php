<?php
 if (isset($_POST["submit"])) {
  $name = htmlspecialchars($_POST['name'], ENT_QUOTES, 'UTF-8');
  $email = htmlspecialchars($_POST['email'], ENT_QUOTES, 'UTF-8');
  $message = htmlspecialchars($_POST['message'], ENT_QUOTES, 'UTF-8');
  $human = intval($_POST['human']);
  $from = 'From: OK!THESS Contact Form <info@okthess.gr>';
  $to = 'mail@okthess.gr';
  $subject = '=?UTF-8?B?' . base64_encode('Μηνυμα από OΚ!THESS website') . '?=';
  $body = "From: $name\n E-Mail: $email\n Message: $message";
  if (!$_POST['name']) {
      $errName = 'Fill in your full name';
  }
  if (!$_POST['email'] || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
      $errEmail = 'The e-mail address is not valid';
  }
  if (!$_POST['message']) {
      $errMessage = 'Παρακαλώ άφησε ένα μήνυμα για να επικοινωνήσουμε πίσω';
  }
  if ($human !== 5) {
      $errHuman = 'Your answer is wrong';
  }
  if (!$errName && !$errEmail && !$errMessage && !$errHuman) {
    if (mail($to, $subject, $body, $from)) {
     $result = '<div class="alert alert-success">Το email σου έχει ληφθεί! Θα επικοινωνήσουμε πίσω το συντομότερο δυνατό</div>';
  } else {
     $result = '<div class="alert alert-danger">Oups!Something went terribly wrong, please try again.</div>';
  }
 }
}
?>
<!DOCTYPE html>
<html lang="en" itemscope itemtype="https://schema.org/ProfessionalService">
<head>
  <meta charset="utf-8"/>
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <title>OK!Thess | Contact Us</title>
  <meta http-equiv="Content-Type" content="text/html">
  <meta name="description" content="Contact Address: Komotinis 2, 54655, Thessaloniki, Greece">
  <meta name="robots" content="NOODP">
  <meta name="author" content="ntemposd">

  <meta itemprop="name" content="OK!Thess">
  <meta itemprop="description" content="Contact Address: Komotinis 2, 54655, Thessaloniki, Greece">
  <meta itemprop="image" content="/img/thumb.png">

  <meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@okthess">
	<meta name="twitter:creator" content="@ntemposd">
	<meta name="twitter:title" content="OK!Thess">
	<meta name="twitter:description" content="Contact Address: Komotinis 2, 54655, Thessaloniki, Greece">
	<meta name="twitter:image" content="http://www.okthess.gr/img/thumb.png">

  <meta property="og:title" content="OK!Thess">
  <meta property="og:description" content="Contact Address: Komotinis 2, 54655, Thessaloniki, Greece">
  <meta property="og:url" content="http://okthess.gr">
  <meta property="og:image" content="/img/thumb.png">
  <meta property="og:type" content="website">

  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="/style/main.css">
  <link rel="stylesheet" type="text/css" href="/style/hi.css">
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
<span id="lang"><a href="http://okthess.gr/hi.php">GR</a></span>
<section class="jumbotron">
  <div class="container">
    <h1>Contact Us</h1>
  </div>
</section>
<div class="container">
 <div class="row">
  <div class="col-md-6">
   <h3>Contact Address</h3>
    <address>
     <abbr title="Thessaloniki's Innovation Ecosystem">OK!THESS</abbr><br>
     <small>Post:</small> Komotinis 2, 54655<br>
     <small>Entrance:</small> Kidonion &amp; Marias Kallas st corner<br>Thessaloniki, Greece.
    </address>
   <h3>Contact through e-mail</h3>
     <form class="form-horizontal" role="form" method="post" action="hi.php">
      <div class="form-group">
       <div class="col-sm-10">
        <textarea class="form-control" rows="1" name="message" placeholder="Your Inquiry"><?php echo htmlspecialchars($_POST['message']); ?></textarea>
         <?php echo "<p class='text-danger'>$errMessage</p>"; ?>
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
        <input type="text" class="form-control" id="name" name="name" placeholder="Full Name" value="<?php echo htmlspecialchars($_POST['name']); ?>">
         <?php echo "<p class='text-danger'>$errName</p>"; ?>
       </div>
      </div>
      <div class="form-group">
       <div class="col-sm-10">
        <input type="text" class="form-control" id="human" name="human" placeholder="Result of (2 + 3 = ?)">
         <?php echo "<p class='text-danger'>$errHuman</p>"; ?>
       </div>
      </div>
      <div class="form-group">
       <div class="col-sm-10">
         <input id="submit" name="submit" type="submit" value="Στείλε!" class="btn btn-primary">
       </div>
      </div>
      <div class="form-group">
       <div class="col-sm-10">
        <?php echo $result; ?>
       </div>
      </div>
    </form>
  </div>
  <div class="col-md-6">
  <h3>Location</h3>
    <div id="map-outer">
      <div id="map-container"></div>
        <script src="/js/map.js"></script>
    </div>
  </div>
 </div>
</div>
<footer class="site-footer">
 <div class="container">
	<div class="row" id="social">
	 <a href="mailto:mail@okthess.gr" target="_blank"><img social src="/img/email.png" alt="email"></a>
	 <a href="https://www.facebook.com/OKThess/" target="_blank"><img social src="/img/facebook.png" alt="facebook"></a>
	 <a href="https://twitter.com/okthess" target="_blank"><img social src="/img/twitter.png" alt="twitter"></a>
	</div>
	<div class="row">
		<div class="col-md-6 col-sm-6">
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
		<div class="col-md-6 col-sm-6">
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
