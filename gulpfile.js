var gulp = require("gulp");
var sass = require("gulp-sass");
var prefix = require("gulp-autoprefixer");
var minify = require("gulp-cssmin");
var browsersync = require("browser-sync");
var del = require('del');
var chalk = require('chalk');

// Compile SASS files into Site.css
gulp.task("build-css", function () {
    log("Building CSS...");
    return gulp
        .src('./static-root/css/style.scss')      
        .pipe(sass().on('error', sass.logError))
        .pipe(prefix())
        // .pipe(minify())
        .pipe(gulp.dest("./static-root/css"))
    .pipe(browsersync.stream());
});

// Browser-sync
gulp.task("sync", function () {
    startBrowserSync();
});

gulp.task('reload', function(){
    browsersync.reload();
});

// Constant watcher for browser-sync and sass-watch
gulp.task("default", ['build-css', 'sync'], function(){
    gulp.watch('./static-root/css/**/*.scss', ['build-css']);
    gulp.watch([
        './static-root/css/**/*.scss',
        './reunion/templates/**/*.html',
        './reunion/**/views.py',
        './static-root/js/**/*.js'
    ], ['reload'])
});


// Utility Functions
function log(msg, color) {
    var color = color ? color : "blue";
    console.log(chalk[color](msg));
}

function startBrowserSync() {
    if (browsersync.active) {
        return;
    }
    console.log("Syncing browsers...");

    var options = {
        proxy: 'localhost:8000/',
        port: 3000,
        files: [
            'templates/**.*',
            'static-root/**/*.scss'
        ],
        ghostMode: {
            click: true,
            scroll: true,
            location: false,
            forms: true
        },
        injectChanges: true,
        logFileChanges: true,
        logLevel: 'debug',
        logPrefix: 'gulp-patterns ' + new Date().toString().split(" ").slice(1, 5).join(" "),
        notify: true,
        reloadDelay: 1000
    };

    browsersync(options);
}
