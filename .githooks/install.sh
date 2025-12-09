#!/bin/bash
# ABOUTME: Installs Git hooks from .githooks/ to .git/hooks/
# ABOUTME: Run this after cloning the repo: bash .githooks/install.sh [--force]

HOOK_DIR=".git/hooks"
SOURCE_DIR=".githooks"
FORCE_INSTALL=false

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -f|--force)
            FORCE_INSTALL=true
            shift
            ;;
        -h|--help)
            echo ""
            echo "Usage: bash .githooks/install.sh [OPTIONS]"
            echo ""
            echo "Options:"
            echo "  -f, --force    Force install, overwrite existing hooks without prompting"
            echo "  -h, --help     Show this help message"
            echo ""
            echo "Examples:"
            echo "  bash .githooks/install.sh           # Install with confirmation prompts"
            echo "  bash .githooks/install.sh --force   # Install without prompts (updates)"
            echo ""
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            echo "Use --help for usage information"
            exit 1
            ;;
    esac
done

echo ""
echo "📦 Installing Git hooks from $SOURCE_DIR..."
[ "$FORCE_INSTALL" = true ] && echo "   (Force mode: will overwrite existing hooks)"
echo ""

# Verify we're in a git repository
if [ ! -d ".git" ]; then
    echo "❌ Error: Not in a git repository root directory"
    echo "Please run this script from the repository root"
    exit 1
fi

# Create hooks directory if it doesn't exist
if [ ! -d "$HOOK_DIR" ]; then
    mkdir -p "$HOOK_DIR"
fi

# Install each hook
INSTALLED_COUNT=0
SKIPPED_COUNT=0
for hook in "$SOURCE_DIR"/*; do
    if [ -f "$hook" ] && [ "$(basename "$hook")" != "install.sh" ]; then
        hook_name=$(basename "$hook")
        target_hook="$HOOK_DIR/$hook_name"

        # Check if hook already exists
        if [ -f "$target_hook" ]; then
            if [ "$FORCE_INSTALL" = false ]; then
                echo "⚠️  Hook '$hook_name' already exists"
                echo ""
                echo "Existing hook preview:"
                head -n 3 "$target_hook" | sed 's/^/    /'
                echo ""
                read -p "Overwrite existing hook? [y/N] " -n 1 -r
                echo ""

                if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                    echo "⏭️  Skipped $hook_name"
                    SKIPPED_COUNT=$((SKIPPED_COUNT + 1))
                    echo ""
                    continue
                fi
                echo ""
            else
                echo "🔄 Overwriting existing $hook_name (force mode)"
            fi
        fi

        # Install the hook
        cp "$hook" "$target_hook"
        chmod +x "$target_hook"
        echo "✅ Installed $hook_name"
        INSTALLED_COUNT=$((INSTALLED_COUNT + 1))
        echo ""
    fi
done

echo ""
echo "═══════════════════════════════════════════════════════════"
echo "Installation Summary"
echo "═══════════════════════════════════════════════════════════"

if [ $INSTALLED_COUNT -eq 0 ] && [ $SKIPPED_COUNT -eq 0 ]; then
    echo "⚠️  No hooks found to install"
else
    [ $INSTALLED_COUNT -gt 0 ] && echo "✅ Installed: $INSTALLED_COUNT hook(s)"
    [ $SKIPPED_COUNT -gt 0 ] && echo "⏭️  Skipped:   $SKIPPED_COUNT hook(s)"
    echo ""

    if [ $INSTALLED_COUNT -gt 0 ]; then
        echo "Hooks will now run automatically during git operations."
        echo ""
        echo "What happens next:"
        echo "  • When you run 'git push', the pre-push hook will validate your MkDocs build"
        echo "  • This catches configuration errors before they reach CI"
        echo "  • Saves time by providing immediate feedback"
        echo ""
        echo "To bypass hooks in emergencies (NOT RECOMMENDED):"
        echo "    git push --no-verify"
    fi
fi
echo ""

exit 0
