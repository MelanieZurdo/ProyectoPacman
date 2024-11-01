import { Component, OnInit } from '@angular/core';
import { NavParams, ModalController } from '@ionic/angular';

@Component({
  selector: 'app-article',
  templateUrl: './article.page.html',
  styleUrls: ['./article.page.scss'],
})
export class ArticlePage implements OnInit {
  article: any;

  constructor(private navParams: NavParams, private modalController: ModalController) {}

  ngOnInit() {
    this.article = this.navParams.get('article');
  }

  /**
   * @function dismissModal
   * @description Funcion que permite al usuario poder cerrar el modal de la noticia seleccionada.
   */
  dismissModal() {
    this.modalController.dismiss();
  }
}