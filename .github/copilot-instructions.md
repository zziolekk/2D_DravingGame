# Copilot instructions for 2D_DravingGame

Short summary
- Small single-module Pygame project. Main game entry: `src.py` in the repository root. Two image assets live in the repo root: `Car.png` and `trace.jpg`.
- Purpose: simple 2D racing demo using Pygame sprites and the main loop in `src.py`.

Big-picture architecture
- Single-script architecture: `src.py` contains initialization (pygame.init()), asset loading, a `Auto` Sprite class, a Pygame display setup and the main loop.
- Assets are loaded at module import time (e.g. `background_image = pygame.image.load("trace.jpg")`). That means importing `src.py` will attempt to load image files immediately.
- Sprite lifecycle: sprites are added to `wszystkie_spritey` (a `pygame.sprite.Group`) and the main loop calls `wszystkie_spritey.update()` and `wszystkie_spritey.draw(ekran)` each frame.

Important project-specific conventions and patterns
- Code uses Polish identifiers (e.g. `ekran`, `wszystkie_spritey`, `aktualizuj`). Keep naming consistent in changes.
- The project currently defines `Auto.aktualizuj(self)` but calls `wszystkie_spritey.update()`. Pygame's Group.update() calls `sprite.update(...)` — i.e. the method must be named `update`. When modifying behavior either:
  - rename `aktualizuj` to `update`, or
  - override Group.update() to call `aktualizuj` on sprites.
  Be explicit and consistent; prefer renaming to `update` for compatibility with Pygame helpers.
- Assets are referenced by filename relative to the repository root. When running from VS Code ensure the working directory is the repo root so `pygame.image.load("trace.jpg")` finds files.

Developer workflows
- Run the game from a terminal in the project root:
  - python src.py
- Ensure Pygame is installed for the interpreter you use in VS Code:
  - python -m pip install pygame
  - Verify with: python -c "import sys, pygame; print(sys.executable, pygame.__version__, pygame.__file__)"
- VS Code tips:
  - Select the same interpreter shown by `python -c "import sys; print(sys.executable)"` using "Python: Select Interpreter".
  - The Run/Debug button may use a different interpreter; prefer running from the integrated terminal when diagnosing ModuleNotFoundError.

Debugging notes (from this codebase)
- Missing module errors usually mean Pygame was installed to a different Python than the one used to run `src.py`. Use `python -m pip show pygame` and validate `sys.executable`.
- Because images are loaded at import time, missing asset files will crash import. If you want to import modules for tests, refactor asset loading into an init function or lazy-load inside `if __name__ == "__main__":`.
- The main game loop currently processes events and then calls `wszystkie_spritey.update()` inside the event loop. Best practice: process all events, then update/draw once per frame (move `wszystkie_spritey.update()` and draw calls outside the event `for` loop). Search `src.py` for the main loop to see the current structure.

Files to inspect when changing behavior
- `src.py` — single source of truth. Check:
  - top-level asset loads (lines near top)
  - `Auto` class (sprite implementation)
  - main loop (event handling, update/draw ordering)
- Repository root — asset files: `Car.png`, `trace.jpg`.

Examples of small edits you may be asked to do
- Rename `def aktualizuj(self):` to `def update(self):` so Group.update() invokes sprite logic.
- Move image loading into a function guarded by `if __name__ == "__main__":` to make the module import-safe for tests.
- Fix main loop indentation/order: call `wszystkie_spritey.update()` and drawing after the event loop, not inside it.

When to ask for clarification
- If a change touches naming conventions (Polish vs English names) — ask whether to keep Polish identifiers.
- If a proposed change alters program start behavior (lazy-loading assets, adding CLI flags) — confirm desired runtime UX.

If you edit files, follow repository patterns:
- Keep variable names and comments in Polish when changing small logic, unless asked to translate.
- Keep assets referenced by relative filenames; do not hardcode absolute paths.

## Instrukcje dla osobistego tutora (tryb nauki)
- Rola: działać jako osobisty tutor Pythona dla początkującego, prowadząc krok po kroku.
- Zasady pracy (użytkownik):
  1. Nie podawać całego rozwiązania od razu. Dostarczać małe fragmenty kodu i tłumaczyć każdą linijkę.
  2. Zadawać pytania przed zaproponowaniem rozwiązania, aby upewnić się, że rozumiemy wymagania.
  3. Tłumaczyć złożone koncepcje prostym językiem, używać analogii i przykładów z życia.
  4. Zachęcać do samodzielnego myślenia — stosować pytania naprowadzające zamiast gotowych odpowiedzi.
  5. Sprawdzać zrozumienie: po wyjaśnieniu dawać krótkie zadania kontrolne i pytania sprawdzające.
  6. Wyjaśniać błędy: nie poprawiać automatycznie kodu użytkownika; opisać błąd i naprowadzić na rozwiązanie.

Dodaj tę sekcję do instrukcji Copilot i stosuj ją przy generowaniu odpowiedzi edukacyjnych dla tego repozytorium.
