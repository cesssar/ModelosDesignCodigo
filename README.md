# Modelos de Design Patterns em Python 🚀

Exemplos de design patterns aplicados na linguagem Python

## 📌 Índice

- [Factory](#factory)
- [Singleton](#singleton)

---

## Factory

O Factory é um padrão de criação que encapsula a lógica de instanciamento de objetos, delegando essa responsabilidade para uma fábrica. Ele permite criar objetos sem expor a lógica de criação ao cliente e promove a reutilização e manutenção do código.

### 🎯 Objetivos

- ✅ Centralizar a criação de objetos.
- ✅ Reduzir o acoplamento entre classes.
- ✅ Melhorar a manutenção e escalabilidade do código.
- ✅ Permitir a criação dinâmica de instâncias de diferentes classes.

### 📌 Quando Usar Factory?

- ✅ Quando a criação de objetos for complexa ou exigir lógica condicional.
- ✅ Para evitar a exposição de classes concretas e promover desacoplamento.
- ✅ Para facilitar a extensão do código sem modificar classes existentes.

---


## Singleton

O Singleton é um padrão de criação que garante que apenas uma instância de uma classe seja criada e fornece um ponto global de acesso a essa instância.

### 🎯 Objetivos

- ✅ Evitar múltiplas instâncias desnecessárias da mesma classe.
- ✅ Controlar o acesso a recursos compartilhados, como conexões de banco de dados, logs e caches.
- ✅ Manter um estado global acessível de forma segura.

### 📌 Quando Usar Singleton?

- ✅ Para gerenciar conexões de banco de dados (evitando múltiplas conexões).
- ✅ Para armazenar configurações globais em um sistema.
- ✅ Para gerenciar logs ou cache compartilhados.
- ✅ Para controlar acesso a recursos limitados, como filas e threads.

