#!/usr/bin/env python3
"""
Allship Record - AI Skills Installer
=====================================

Tự động cài đặt AI Skills từ repository:
https://github.com/sickn33/antigravity-awesome-skills

Usage:
    python install_skills.py              # Cài đặt tất cả skills
    python install_skills.py --list       # Liệt kê skills sẽ cài
    python install_skills.py --update     # Cập nhật skills đã có
    python install_skills.py --clean      # Xóa và cài lại
"""

import os
import sys
import shutil
import subprocess
import argparse
from pathlib import Path

# =============================================================================
# CONFIGURATION
# =============================================================================

# Repository chứa skills
SKILLS_REPO = "https://github.com/sickn33/antigravity-awesome-skills.git"

# Đường dẫn thư mục skills trong dự án
SKILLS_DIR = Path(__file__).parent / "skills"

# Danh sách skills cần cài đặt (từ PROJECT_SKILLS.md)
# Format: folder_name
REQUIRED_SKILLS = [
    # Nhóm 1: Kiến Trúc & Thiết Kế
    "03_software-architecture",
    "04_database-design",
    "11_architecture-decision-records",
    
    # Nhóm 2: Phát Triển Mobile (Flutter)
    "01_flutter-expert",
    "02_mobile-design",
    
    # Nhóm 3: Phát Triển Desktop & Web
    "08_typescript-pro",
    "16_browser-extension-builder",
    
    # Nhóm 4: Video & Media Processing
    "17_video-encoding-mobile",
    
    # Nhóm 5: Hardware Integration
    "18_barcode-scanning-integration",
    "19_bluetooth-hid-integration",
    "20_rtsp-ip-camera",
    
    # Nhóm 6: API & Backend
    "09_api-design-principles",
    
    # Nhóm 7: Testing & Quality
    "05_error-handling-patterns",
    "06_testing-patterns",
    "10_debugging-strategies",
    "15_clean-code",
    "21_performance-optimization",
    "22_mobile-security",
    
    # Nhóm 8: UI/UX Design
    "23_ui-ux-pro-max",
    
    # Nhóm 9: Planning & Documentation
    "07_plan-writing",
    "12_brainstorming",
    "13_product-manager-toolkit",
    "14_documentation-templates",
]

# =============================================================================
# COLORS FOR OUTPUT
# =============================================================================

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_header(msg):
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{msg}{Colors.END}")
    print(f"{Colors.HEADER}{Colors.BOLD}{'='*60}{Colors.END}\n")

def print_success(msg):
    print(f"{Colors.GREEN}✔ {msg}{Colors.END}")

def print_error(msg):
    print(f"{Colors.FAIL}✖ {msg}{Colors.END}")

def print_warning(msg):
    print(f"{Colors.WARNING}⚠ {msg}{Colors.END}")

def print_info(msg):
    print(f"{Colors.CYAN}ℹ {msg}{Colors.END}")

# =============================================================================
# FUNCTIONS
# =============================================================================

def check_git():
    """Kiểm tra git đã được cài đặt chưa"""
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def clone_repo(temp_dir: Path) -> bool:
    """Clone repository skills vào thư mục tạm"""
    print_info(f"Đang clone repository từ {SKILLS_REPO}...")
    
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", SKILLS_REPO, str(temp_dir)],
            capture_output=True,
            check=True,
            text=True
        )
        print_success("Clone repository thành công!")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Không thể clone repository: {e.stderr}")
        return False

def copy_skills(temp_dir: Path, skills_list: list) -> tuple:
    """Copy các skills cần thiết từ thư mục tạm"""
    installed = []
    skipped = []
    missing = []
    
    for skill in skills_list:
        source = temp_dir / skill
        dest = SKILLS_DIR / skill
        
        if not source.exists():
            print_warning(f"Skill không tìm thấy trong repo: {skill}")
            missing.append(skill)
            continue
        
        if dest.exists():
            print_info(f"Skill đã tồn tại, bỏ qua: {skill}")
            skipped.append(skill)
            continue
        
        try:
            shutil.copytree(source, dest)
            print_success(f"Đã cài đặt: {skill}")
            installed.append(skill)
        except Exception as e:
            print_error(f"Không thể copy {skill}: {e}")
            missing.append(skill)
    
    return installed, skipped, missing

def update_skills(temp_dir: Path, skills_list: list) -> tuple:
    """Cập nhật các skills đã có"""
    updated = []
    missing = []
    
    for skill in skills_list:
        source = temp_dir / skill
        dest = SKILLS_DIR / skill
        
        if not source.exists():
            print_warning(f"Skill không tìm thấy trong repo: {skill}")
            missing.append(skill)
            continue
        
        # Xóa skill cũ nếu có
        if dest.exists():
            shutil.rmtree(dest)
        
        try:
            shutil.copytree(source, dest)
            print_success(f"Đã cập nhật: {skill}")
            updated.append(skill)
        except Exception as e:
            print_error(f"Không thể cập nhật {skill}: {e}")
            missing.append(skill)
    
    return updated, missing

def clean_skills():
    """Xóa tất cả skills đã cài"""
    if SKILLS_DIR.exists():
        print_warning("Đang xóa thư mục skills...")
        shutil.rmtree(SKILLS_DIR)
        print_success("Đã xóa thư mục skills!")
    else:
        print_info("Thư mục skills không tồn tại.")

def list_skills():
    """Liệt kê các skills sẽ được cài đặt"""
    print_header("DANH SÁCH SKILLS")
    
    total = len(REQUIRED_SKILLS)
    installed = 0
    missing = 0
    
    for skill in REQUIRED_SKILLS:
        dest = SKILLS_DIR / skill
        if dest.exists():
            print_success(f"{skill} (đã cài)")
            installed += 1
        else:
            print_warning(f"{skill} (chưa cài)")
            missing += 1
    
    print(f"\n{Colors.BOLD}Tổng: {total} skills | Đã cài: {installed} | Chưa cài: {missing}{Colors.END}")

def remove_git_folder():
    """Xóa thư mục .git trong skills để tránh embedded repo"""
    git_dir = SKILLS_DIR / ".git"
    if git_dir.exists():
        shutil.rmtree(git_dir)
        print_success("Đã xóa .git trong thư mục skills")

# =============================================================================
# MAIN
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="Cài đặt AI Skills cho Allship Record"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="Liệt kê danh sách skills"
    )
    parser.add_argument(
        "--update", "-u",
        action="store_true",
        help="Cập nhật skills đã cài"
    )
    parser.add_argument(
        "--clean", "-c",
        action="store_true",
        help="Xóa và cài lại tất cả skills"
    )
    
    args = parser.parse_args()
    
    print_header("ALLSHIP RECORD - AI SKILLS INSTALLER")
    
    # Liệt kê skills
    if args.list:
        list_skills()
        return 0
    
    # Kiểm tra git
    if not check_git():
        print_error("Git chưa được cài đặt! Vui lòng cài đặt git trước.")
        return 1
    
    # Clean nếu được yêu cầu
    if args.clean:
        clean_skills()
    
    # Tạo thư mục skills nếu chưa có
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Tạo thư mục tạm
    temp_dir = Path.cwd() / ".temp_skills"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    
    try:
        # Clone repository
        if not clone_repo(temp_dir):
            return 1
        
        # Copy hoặc update skills
        if args.update:
            print_header("CẬP NHẬT SKILLS")
            updated, missing = update_skills(temp_dir, REQUIRED_SKILLS)
            
            print(f"\n{Colors.BOLD}Kết quả:{Colors.END}")
            print(f"  Đã cập nhật: {len(updated)} skills")
            print(f"  Không tìm thấy: {len(missing)} skills")
        else:
            print_header("CÀI ĐẶT SKILLS")
            installed, skipped, missing = copy_skills(temp_dir, REQUIRED_SKILLS)
            
            print(f"\n{Colors.BOLD}Kết quả:{Colors.END}")
            print(f"  Đã cài mới: {len(installed)} skills")
            print(f"  Đã bỏ qua: {len(skipped)} skills")
            print(f"  Không tìm thấy: {len(missing)} skills")
        
        # Xóa .git folder nếu có
        remove_git_folder()
        
        print_success("\nHoàn thành!")
        return 0
        
    finally:
        # Cleanup thư mục tạm
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
            print_info("Đã xóa thư mục tạm")


if __name__ == "__main__":
    sys.exit(main())
