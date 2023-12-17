require 'bundler/setup'

require 'sinatra'
require 'haml'
require 'nokogiri'
require 'open-uri'

set :haml, format: :html5
enable :sessions

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
  if titulo == ''
    titulo = ' '
  else
    titulo = titulo.reverse[10..].reverse
  end
  return titulo
end


linhas = File.readlines('public/url', chomp: true)
nomes = [{}, {}, {}, {}, {}]

get '/' do
  @url = pegaLinha(linhas)
  @titulo = pegaTitulo(@url)
  @nomes = nomes
  haml :index 
end

post '/a' do
  id = params["id"].to_i
  nomes[id-1]["url"] = "https://youtu.be/"+params["url"]
  nomes[id-1]["titulo"] = params["titulo"]
  redirect to('/')
end

get '/resetar' do
  linhas = File.readlines('public/url', chomp: true)
  nomes = [{}, {}, {}, {}, {}]
  redirect to('/')
end

