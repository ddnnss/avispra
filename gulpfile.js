var gulp = require('gulp');
    sass        = require('gulp-sass');
    browserSync = require('browser-sync');
    autoprefixer = require('gulp-autoprefixer')
gulp.task('sass', function(){
    return gulp.src('html/sass/**/*.sass')
        .pipe(sass())
        .pipe(autoprefixer({
            browsers: ['last 4 versions']
        }))
        .pipe(gulp.dest('html/css'))
        .pipe(browserSync.reload({stream: true}))
});

gulp.task('browser-sync', function() {
    browserSync({
        browser: 'chrome',
        server: {
            baseDir: 'html'
        },
        notify: false
    });
});

gulp.task('scripts', function() {
    return gulp.src(['html/js/main.js', 'html/libs/**/*.js'])
    .pipe(browserSync.reload({ stream: true }))
});

gulp.task('code', function() {
    return gulp.src('html/*.html')
    .pipe(browserSync.reload({ stream: true }))
});

gulp.task('watch', function() {
    gulp.watch('html/sass/**/*.sass', gulp.parallel('sass'));
    gulp.watch('html/*.html', gulp.parallel('code'));
    gulp.watch(['html/js/main.js', 'html/libs/**/*.js'], gulp.parallel('scripts'));
});

gulp.task('default', gulp.parallel('sass', 'browser-sync', 'watch'));

