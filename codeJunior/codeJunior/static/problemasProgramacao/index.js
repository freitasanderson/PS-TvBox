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

const formSubmeterDesafio = document.querySelector('#formSubmeterDesafio')
const containerLoadingButton = document.querySelector('#containerLoadingButton')
const containerResultado = document.querySelector('#containerResultado')
const containerEditor = document.querySelector('#containerEditor')

async function submeterDesafioAPI(url, formElement) {
  addLoad(containerLoadingButton)
  escreverResultado(`
  <h1 class="text-green-500 flex items-center gap-2"><span class="text-4xl font-bold ">Processando código </span><i class="mr-2 h-4 w-4 animate-spin fa-solid fa-circle-notch"></i></h1>
  `)

  const crf_token = document.querySelector('[name="csrfmiddlewaretoken"]').value

  const data = new URLSearchParams();
  for (const pair of new FormData(formElement)) {
      data.append(pair[0], pair[1]);
  }

  const response = await fetch(url, { 
    method: 'post',
    processData: false,
    headers: {
      "Conten-Type": "application/json",
      "X-CSRFToken": crf_token
    },
    body: data
  });

  const responseJson = await response.json()
  const [obj] = JSON.parse(responseJson);
  console.log(obj.correta)
  if (obj.correta) {
    escreverResultado(`
    <h1 class="text-green-500 flex items-center gap-2"><span class="text-4xl font-bold ">Parabens <i class="fa-solid fa-circle-check"></i></h1>
        <div class="mt-4 text-slate-100">
          <div>
            <small>Compiler Message</small>
            <p class="mt-1 p-4 bg-slate-900 w-full">Reposta correta</p>
          </div>

          <div class="mt-4">
            <small>Expected Output</small>
            
            <ul>
              <li class="flex mt-1 bg-slate-900 w-full ">
                <span class="p-4 border-r-1">1</span>
                <p class="p-4 font-bold">${obj.entrada}</p>
              </li>
            </ul>
          </div>
        </div>
    `)
  } else {
    escreverResultado(`
    <h1 class="text-red-500 flex items-center gap-2"><span class="text-4xl font-bold ">O teste falhou <i class="fa-solid fa-circle-xmark"></i></h1>
        <div class="mt-4 text-slate-100">
          <div>
            <small>Compiler Message</small>
            <p class="mt-1 p-4 bg-slate-900 w-full">Reposta incorreta</p>
          </div>

          <div class="mt-4">
            <small>Expected Output</small>
            
            <ul>
              <li class="flex mt-1 bg-slate-900 w-full ">
                <span class="p-4 border-r-1">1</span>
                <p class="p-4 font-bold">${obj.entrada}</p>
              </li>
            </ul>
          </div>
        </div>
    `)
  }

  setTimeout(() => {
    removeLoad(containerLoadingButton)
  }, 500)

}

function addLoad(element) {
  element.innerHTML = `
    <div class="containerCarregamento">
      <i class="mr-2 h-4 w-4 animate-spin fa-solid fa-circle-notch"></i>
    </div>
  `
}

function removeLoad(element) {
  element.innerHTML = ``
}

function escreverResultado(html) {
  containerResultado.innerHTML = ''
  containerEditor.classList.remove('grid-rows-[1fr_0rem]')
  containerEditor.classList.add('grid-rows-[1fr_20rem]')

  containerResultado.innerHTML = html
}

formSubmeterDesafio.addEventListener('submit', (evt) => {
  evt.preventDefault()

  const problema = formSubmeterDesafio.elements.problema.value
  const pessoa = formSubmeterDesafio.elements.pessoa.value
  const codigo = formSubmeterDesafio.elements.codigo.value

  const url = new URL(formSubmeterDesafio.action)
  problema && url.searchParams.append('problema', problema)
  pessoa && url.searchParams.append('pessoa', pessoa)
  codigo && url.searchParams.append('codigo', codigo)

  submeterDesafioAPI(url, formSubmeterDesafio)
})