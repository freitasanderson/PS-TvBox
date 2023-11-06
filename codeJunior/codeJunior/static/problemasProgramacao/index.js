const textarea = document.querySelector('[name="codigo"]')
const editorEl = document.querySelector('.editor');
const editor = window.ace.edit(editorEl);
editor.setTheme(`ace/theme/dracula`);
editor.session.setMode(`ace/mode/python`);
editor.setFontSize(18)
editor.on('change', data => {
  console.log('edited result', data);
  textarea.value = (editor.getSession().getValue());
});