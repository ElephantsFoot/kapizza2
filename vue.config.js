module.exports = {
  assetsDir: '',
  outputDir: 'flask_kapizza2/static',
  publicPath: '/static/',
  devServer: {
    proxy: {
      '^/*': {
        target: 'http://localhost:5000/',
      },
    },
  },
};
