require 'bundler/setup'

require 'sinatra'
require 'haml'
require 'nokogiri'
require 'open-uri'

# sinatra config
set :haml, format: :html5
enable :sessions


# getters
def pegaLinha linhas
  l = linhas.sample
  linhas.delete(l)
  return l  
end

def pegaTitulo url
  fullURL = "http://youtu.be/" + url
  html = URI.open(fullURL).read
  doc = Nokogiri::HTML(html, nil, 'UTF-8')
  titulo = doc.at_css('title').text
  titulo = titulo.reverse[10..].reverse
  if titulo == ''
    titulo = '.'
  end

  return titulo
end

# variables
linhas = File.readlines('public/url', chomp: true)


# routing
get '/' do
  @url = pegaLinha(linhas)
  @titulo = pegaTitulo(@url)
  @nomes = session[:nomes] || Array.new(5, {})
<<<<<<< HEAD
  haml :index
=======
  
  haml :index 
>>>>>>> 27c0ab5b4ffa2e76b6c1807838541640067aaabc
end

post '/a' do
  id = params["id"].to_i
  token = params["url"]
  url = "https://youtu.be/"+params["url"]
  titulo = params[:titulo]
  
  lH = session[:nomes] || Array.new(5, {})
  lH[id-1] = {"token" => token, "url" => url, "titulo" => titulo}
  
  session[:nomes] = lH
  
  redirect to('/')
end

get '/resetar' do
  linhas = File.readlines('public/url', chomp: true)
  session[:nomes] = [{}, {}, {}, {}, {}]
  redirect to('/')
end

get '/instrucoes' do
  haml :instrucoes
end
