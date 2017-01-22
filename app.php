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
          $errName = 'Συμπλήρωσε το όνομα σου';
      }
      if (!$_POST['email'] || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
          $errEmail = 'Η διεύθυνση email δεν είναι υπαρκτή';
      }
      if (!$_POST['phone']) {
          $errPhone = 'Συμπλήρωσε το τηλέφωνο σου';
      }
      if (!$_POST['message1']) {
          $errMessage1 = 'Υποχρεώτικό πεδίο';
      }
      if (!$_POST['message2']) {
          $errMessage2 = 'Υποχρεώτικό πεδίο';
      }
      if (!$_POST['message3']) {
          $errMessage3 = 'Υποχρεώτικό πεδίο';
      }
      if (!$_POST['message4']) {
          $errMessage4 = 'Υποχρεώτικό πεδίο';
      }
      if ($human !== 5) {
          $errHuman = 'Η απάντηση δεν είναι σωστή';
      }
      if (!$errName && !$errEmail && !$errMessage1 && !$errHuman) {
          if (mail($to, $subject, $body, $from)) {
            $result = '<div class="alert alert-success">Το email σου έχει ληφθεί! Θα ενημερωθείς για την πορεία της αίτησης σου με την ολοκλήρωση της διαδικασίας αξιολόγησης.</div>';
          } else {
            $result = '<div class="alert alert-danger">Ουπς! Προέκυψε ένα λάθος, δοκίμασε ξανά.</div>';
      }
     }
    }
?>
<!DOCTYPE html>
<html lang="gr" itemscope itemtype="https://schema.org/ProfessionalService">
<head>
  <meta charset="utf-8"/>
  <meta http-equiv="encoding" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="icon" href="/img/favicon.png" type="image/png" sizes="32x32">

  <title>OK!Thess | Αίτηση Συμμετοχής</title>
  <meta http-equiv="Content-Type" content="text/html">
  <meta name="description" content="Γίνονται δεκτές καινοτόμες προτάσεις από άτομα ή ομάδες, ανεξάρτητα του βαθμού ωρίμανσης, που θα ήθελαν να ωφεληθούν από τις υπηρεσίες της προ-θερμοκοιτίδας του OK!Thess.">
  <meta name="robots" content="NOODP">
  <meta name="author" content="ntemposd">

  <meta itemprop="name" content="OK!Thess">
  <meta itemprop="description" content="Γίνονται δεκτές καινοτόμες προτάσεις από άτομα ή ομάδες, ανεξάρτητα του βαθμού ωρίμανσης, που θα ήθελαν να ωφεληθούν από τις υπηρεσίες της προ-θερμοκοιτίδας του OK!Thess.">
  <meta itemprop="image" content="/img/thumb.png">

  <meta name="twitter:card" content="summary_large_image">
	<meta name="twitter:site" content="@okthess">
	<meta name="twitter:creator" content="@ntemposd">
	<meta name="twitter:title" content="OK!Thess">
	<meta name="twitter:description" content="Γίνονται δεκτές καινοτόμες προτάσεις από άτομα ή ομάδες, ανεξάρτητα του βαθμού ωρίμανσης, που θα ήθελαν να ωφεληθούν από τις υπηρεσίες της προ-θερμοκοιτίδας του OK!Thess.">
	<meta name="twitter:image" content="http://www.okthess.gr/img/thumb.png">

  <meta property="og:title" content="OK!Thess">
  <meta property="og:description" content="Γίνονται δεκτές καινοτόμες προτάσεις από άτομα ή ομάδες, ανεξάρτητα του βαθμού ωρίμανσης, που θα ήθελαν να ωφεληθούν από τις υπηρεσίες της προ-θερμοκοιτίδας του OK!Thess.">
  <meta property="og:url" content="http://okthess.gr">
  <meta property="og:image" content="/img/thumb.png">
  <meta property="og:type" content="website">

  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="http://okthess.gr/dev/style/main.css">
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
    <a class="navbar-brand" href="index.html"><img src="img/logo.png" alt="Logo"></a>
  </div>
  <div class="collapse navbar-collapse" id="navbar-collapse">
   <ul class="nav navbar-nav navbar-right">
    <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">Σχετικά <b class="caret"></b></a>
     <ul class="dropdown-menu">
      <li><a tabindex="-1" href="about.html#collapse0">Τι κάνουμε</a></li>
      <li><a tabindex="-1" href="about.html#collapse1">Πως το κάνουμε</a></li>
      <li><a tabindex="-1" href="about.html#collapse2">Πως συμμετέχω</a></li>
      <li><a tabindex="-1" href="about.html#collapse3">Συνεργατικός χώρος</a></li>
     </ul>
    </li>
    <li><a href="teams.html">Ομάδες</a></li>
    <li><a href="news.html">Νέα</a></li>
    <li><a href="knowledge-base.html">Γνωσιακή Βάση</a></li>
    <li class="active"><a href="app.php">Συμμετοχή</a></li>
    <li><a href="hi.php">Επικοινωνία</a></li>
   </ul>
  </div>
</nav>
<div class="container">
 <div class="row text-center" id="teams">
	<div class="text-center" id="call">
		<h1><strong>Αίτηση Συμμετοχής</strong></h1>
    <p>Πληροφορίες και φόρμα συμμετοχής για το πρόγραμμα επιτάχυνσης του OK!Thess.</p>
		<br>
	</div>
 </div>
</div>
<div class="container">
  <p>Γίνονται δεκτές ανά πάσα στιγμή προτάσεις από άτομα ή ομάδες με καινοτόμες ιδέες, ανεξάρτητα του βαθμού ωρίμανσης, που θα ήθελαν να ωφεληθούν από τις υπηρεσίες της προ-θερμοκοιτίδας του OK!Thess ώστε να στήσουν μια επιχείρηση (startup) ή να ενισχύσουν μια startup που έχουν ήδη στήσει.</p>
  <p>Οι προτάσεις αξιολογούνται σε τακτά χρονικά διαστήματα, οι ακριβείς ημερομηνίες ανακοινώνονται στην παρούσα ιστοσελίδα. Η τελευταία περίοδος αξιολόγησης έκλεισε την 1η Δεκέμβρη 2016 και η επόμενη έχει προγραμματιστεί για τις αρχές του 2017. Η ακριβής ημερομηνία θα ανακοινωθεί στο αμέσως προσεχές μέλλον.</p>
  <p>Για συμμετοχή συμπληρώστε την παρακάτω φόρμα συμμετοχής ή απαντήστε τις ερωτήσεις στο σώμα ενός e-mail και στείλτε στο <strong><small>apply@okthess.gr</small></strong></p>
  <br>
  <a class="btn btn-primary" href="http://okthess.gr/pdf/website-open-call.pdf" role="button" target="_blank">Πληροφορίες</a>
  <a class="btn btn-primary" href="http://okthess.gr/under-construction.html" role="button" target="_blank">Eσωτερικός κανονισμός</a>
  <br>
  <br>
  <h2 class="text-muted">Φόρμα Συμμετοχής</h2>
  ---------------
  <form class="form-horizontal" role="form" method="post" action="app.php">
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message1" placeholder="Ποιά είναι η επιχειρηματική ιδέα που θέλετε να αναπτύξετε στο OK!Thess (Έως 150 λέξεις);"><?php echo htmlspecialchars($_POST['message1']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage1</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message2" placeholder="Σε ποιά αγορά απευθύνεσθε (πού βλέπετε τους μελλοντικούς πελάτες) (έως 100 λέξεις);"><?php echo htmlspecialchars($_POST['message2']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage2</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message3" placeholder="Γνωρίζετε ποιος είναι ο ανταγωνισμός στην ιδέα σας (έως 100 λέξεις);"><?php echo htmlspecialchars($_POST['message3']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage3</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <textarea class="form-control" rows="2" name="message4" placeholder="Τι περιμένετε να σας προσφέρει το OK!Thess εκτός από χώρο και υποδομή (έως 100 λέξεις);"><?php echo htmlspecialchars($_POST['message4']); ?></textarea>
          <?php echo "<p class='text-danger'>$errMessage4</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="text" class="form-control" id="phone" name="phone" placeholder="Τηλέφωνο επικοινωνίας" value="<?php echo htmlspecialchars($_POST['phone']); ?>">
          <?php echo "<p class='text-danger'>$errPhone</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="email" class="form-control" id="email" name="email" placeholder="email" value="<?php echo htmlspecialchars($_POST['email']); ?>">
          <?php echo "<p class='text-danger'>$errEmail</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="text" class="form-control" id="name" name="name" placeholder="Ονοματεπώνυμο" value="<?php echo htmlspecialchars($_POST['name']); ?>">
          <?php echo "<p class='text-danger'>$errName</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input type="number" class="form-control" id="human" name="human" placeholder="Και το αποτέλεσμα της πράξης (2 + 3 = ?)">
          <?php echo "<p class='text-danger'>$errHuman</p>"; ?>
      </div>
    </div>
    <div class="form-group">
      <div class="col-sm-10">
        <input id="submit" name="submit" type="submit" value="Αποστολή" class="btn btn-primary">
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
			<a href="mailto:mail@okthess.gr" target="_blank"><img social src="http://okthess.gr/dev/img/email.png" alt="email"></a>
			<a href="https://www.facebook.com/OKThess/" target="_blank"><img social src="http://okthess.gr/dev/img/facebook.png" alt="facebook"></a>
			<a href="https://twitter.com/okthess" target="_blank"><img social src="http://okthess.gr/dev/img/twitter.png" alt="twitter"></a>
		</div>
		<div class="row">
			<div class="col-md-4 col-sm-4">
				<h5>ΤΟΠΟΘΕΣΙΑ</h5>
				<hr>
					<div id="map-outer">
						<div id="map-container"></div>
						<script src="/js/map.js"></script>
					</div>
			</div>
			<div class="col-md-4 col-sm-4">
				<h5>ΣΥΝΕΡΓΑΤΕΣ</h5><hr>
  				<a href="https://www.auth.gr/" target="_blank"><img src="http://okthess.gr/dev/img/AUTH.jpg" alt="Aristotle_University_Thessaloniki"></a>
  				<a href="http://www.thessaloniki.gr/" target="_blank"><img src="http://okthess.gr/dev/img/municipality.jpg" alt="Municipality_of_Thessaloniki"></a>
  				<a href="http://www.uom.gr/" target="_blank"><img src="http://okthess.gr/dev/img/UOM.png" alt="University_Of_Macedonia"></a>
  				<a href="http://www.thessinnozone.gr/" target="_blank"><img src="http://okthess.gr/dev/img/TIZ.jpg" alt="Thessaloniki_Innovation_Zone"></a>
  				<a href="http://www.teithe.gr/" target="_blank"><img src="http://okthess.gr/dev/img/ATEITH.jpg" alt="Alexander_Technological_Institute_Thessaloniki"></a>
  				<a href="http://www.sbbe.gr/" target="_blank"><img src="http://okthess.gr/dev/img/SBBE.jpg" alt="SBBE"></a>
  				<a href="http://www.ihu.edu.gr/" target="_blank"><img src="http://okthess.gr/dev/img/IHU.jpg" alt="International_Hellenic_University"></a>
  				<a href="http://www.seve.gr/" target="_blank"><img src="http://okthess.gr/dev/img/SEVE.jpg" alt="SEVE"></a>
			</div>
			<div class="col-md-4 col-sm-4">
				<h5>ΥΠΟΣΤΗΡΙΚΤΕΣ</h5><hr>
				<a href="http://www.hcn.gr/" target="_blank"><img src="http://okthess.gr/dev/img/hcn.jpg" alt="HCN"></a>
				<a href="http://www.beetroot.gr/" target="_blank"><img src="http://okthess.gr/dev/img/beetroot.png" alt="Beetroot"></a>
				<a href="https://www.ast.gr/" target="_blank"><img src="http://okthess.gr/dev/img/ast.png" alt="AST"></a>
				<h5>ΔΩΡΗΤΗΣ</h5><hr>
				<a href="http://www.snf.org/el/" target="_blank"><img src="http://okthess.gr/dev/img/ISN.jpg" alt="ISN"></a>
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
