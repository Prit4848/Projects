const express = require('express');
const app = express();
const path = require('path');

app.use(express.json());
app.use(express.urlencoded({extended:true}));
app.use(express.static(path.join(__dirname,'public')));// this can use to give path of public folder 
app.set('view engine','ejs'); // we can use egs file write this

app.get("/",function(req,res){
    res.render("index")
});
app.get("/public/:name",function(req,res){  //we can use collun this part was dynamic matlab kuch bi likh sakte hai
    res.send(`well come,${req.params.username}`)
})
app.get("/public/:name/:age",function(req,res){
    res.send(`well come,${req.params.name} ${req.params.age}`)
})

app.listen(3000,function(){
    console.log("starting the code !!")
})