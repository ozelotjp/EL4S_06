var express = require('express');
var router = express.Router();
var multer = require('multer')
var storage = multer.diskStorage({
  destination: function(req, file, cb){
    cb(null, '/home/nhs/EL4S/myapp/public/images/')
  },
  filename: function(req, file, cb){
    cb(null, 'image.jpg')
  }
})
var upload = multer({storage: storage})
var { PythonShell } = require('python-shell');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Index' });
});

router.post("/result", upload.single('image'), (req, res, next) => {
  PythonShell.run('/home/nhs/EL4S/main.py', null, function (err) {
    if (err) throw err;
    res.render('result', { title: 'Result' });
  });
});

module.exports = router;
