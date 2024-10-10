document.getElementById('sign-up').addEventListener('click', function() {
  document.querySelector('.login').classList.add('hide');
  document.querySelector('.register').classList.remove('hide');
});

document.getElementById('sign-in').addEventListener('click', function() {
  document.querySelector('.register').classList.add('hide');
  document.querySelector('.login').classList.remove('hide');
});
