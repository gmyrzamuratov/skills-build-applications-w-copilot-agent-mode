module.exports = {
  launch: {
    command: 'npm start',
    cwd: __dirname,
    port: 3000,
    waitOnScheme: 'http',
    waitOnTimeout: 60000,
    env: {
      BROWSER: 'none'
    }
  }
};
