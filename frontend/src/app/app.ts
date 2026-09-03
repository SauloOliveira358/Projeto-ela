import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  // 1. Criando uma variável TypeScript
  usuario: string = 'Saulo';

  // 2. Criando uma função
  mudarNome() {
    this.usuario = 'Administrador Projeto Ela';
  }
}
