import { Component, OnInit } from '@angular/core';
import { NavController } from '@ionic/angular';

import { ModalController } from '@ionic/angular';
import { Article } from 'src/app/models/article.model';

import { UtilsService } from 'src/app/services/utils.service';
import { NewsService } from 'src/app/services/news.service';
import { ArticlePage } from './article/article.page';

@Component({
  selector: 'app-tab1',
  templateUrl: 'tab1.page.html',
  styleUrls: ['tab1.page.scss']
})
export class Tab1Page implements OnInit {

  news: Article[] = [];
  categories = ['business', 'general', 'science', 'technology', 'sports'];
  selectedCategory = 'general';
  newsArticles = [];

  constructor(
    private newsService: NewsService,
    private utilsService: UtilsService,
    private modalController: ModalController,
    private navCtrl: NavController
  ) {}

  ngOnInit() {
    this.loadNews();
    };
  
    /**
     * @function loadNews
     * @description Funcion que se encarga de ejecutar la consulta de las noticias a la API
     */
    loadNews() {
      this.newsService.getNews(this.selectedCategory).subscribe((response) => {
        this.newsArticles = response.data;
        this.loadInLocalStorageFirstTenNews();
      })
    }

    /**
     * @function loadInLocalStorageFirstTenNews
     * @description Funcion que realiza el guardado de las primeras 10 noticias obtenidas en el local 
     * storage, bajo el identificador 'firstTenNews'
     */
    loadInLocalStorageFirstTenNews() {
      const firstTenNews = this.newsArticles.slice(0, 10);
      this.utilsService.saveInLocalStorage('firstTenNews', firstTenNews);
    }

    /**
     * @function onCategoryChange
     * @description Funcion que recibe el parametro por el cual el usuario selecciono el filtrado en las 
     * pills y ejecuta una nueva busqueda por la categoria seleccionada
     * @param category - recibe la categoria seleccionada
     */
    onCategoryChange(category: any) {
      this.selectedCategory = String(category);
      this.loadNews();
    }

    /**
     * @function openArticle
     * @description Funcion para que el usuario pueda ver mas detalle de una noticia seleccionada haciendo 
     * click con el dedo sobre la misma. Se abre un modal con mas informacion.
     * @param article - recibe el articulo puntual que el usuario selecciono
     */
    async openArticle(article: Article) {
    const modal = await this.modalController.create({
      component: ArticlePage,
      componentProps: { article }
    });
    return await modal.present();
  }

}