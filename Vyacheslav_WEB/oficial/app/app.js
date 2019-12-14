var fs = require('fs');
var http = require('http');
var https = require('https');

// Certificate
const privateKey = fs.readFileSync('/etc/letsencrypt/live/goodstampa.com/privkey.pem', 'utf8');
const certificate = fs.readFileSync('/etc/letsencrypt/live/goodstampa.com/cert.pem', 'utf8');
const ca = fs.readFileSync('/etc/letsencrypt/live/goodstampa.com/fullchain.pem', 'utf8');

const credentials = {
        key: privateKey,
        cert: certificate,
        ca: ca
};

const local_app = function () {}
// * ———————————————————————————————————————————————————————— * //
// * 	init
// *
// *	gets called upon starting enduro.js production server
// *	@param {express app} app - express app
// *	@return {nothing}
// * ———————————————————————————————————————————————————————— * //
local_app.prototype.init = function (app) {
	app.use (function (req, res, next) {
        if (req.secure) {
                // request was via https, so do no special handling
                next();
        } else {
                // request was via http, so redirect to https
                res.redirect('https://' + req.headers.host + req.url);
        }
    });
    var httpServer = http.createServer(app);
    var httpsServer = https.createServer(credentials, app);

    httpServer.listen(80);
    console.log("Escuchando en el 80");
    httpsServer.listen(443);

}

module.exports = new local_app()
