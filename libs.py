import pandas as pd
import os
from datetime import datetime

class MoodEntry:
    def __init__(self, date, mood, journal_entry):
        self.date = date
        self.mood = mood
        self.journal_entry = journal_entry if journal_entry and str(journal_entry).lower() != "nan" else "-"
    
    def update_mood(self, mood):
        self.mood = mood
        return self
    
    def update_journal(self, journal_entry):
        self.journal_entry = journal_entry if journal_entry and str(journal_entry).lower() != "nan" else "-"
        return self
    
    def get_formatted_date(self):
        date_obj = datetime.strptime(self.date, "%Y-%m-%d") if isinstance(self.date, str) else self.date
        return date_obj.strftime("%d %B %Y")
    
    def to_dict(self):
        return {
            "date": self.date if isinstance(self.date, str) else self.date.strftime("%Y-%m-%d"),
            "mood": self.mood,
            "journal_entry": self.journal_entry
        }


class MoodJournal:
    def __init__(self, data_file="data/mood_journal.csv"):
        self.data_file = data_file
        self.entries = []
        self._ensure_data_file_exists()
        self.load_entries()
    
    def _ensure_data_file_exists(self):
        data_dir = os.path.dirname(self.data_file)
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            
        if not os.path.exists(self.data_file):
            df = pd.DataFrame(columns=["date", "mood", "journal_entry"])
            df.to_csv(self.data_file, index=False)
    
    def load_entries(self):
        df = pd.read_csv(self.data_file)
        self.entries = []
        
        for _, row in df.iterrows():
            journal_text = row["journal_entry"] if pd.notna(row["journal_entry"]) else "-"
            entry = MoodEntry(
                date=row["date"],
                mood=row["mood"],
                journal_entry=journal_text
            )
            self.entries.append(entry)
    
    def save_entries(self):
        if not self.entries:
            df = pd.DataFrame(columns=["date", "mood", "journal_entry"])
        else:
            entries_data = [entry.to_dict() for entry in self.entries]
            df = pd.DataFrame(entries_data)
        
        df.to_csv(self.data_file, index=False)
    
    def add_entry(self, entry):
        date_str = entry.date if isinstance(entry.date, str) else entry.date.strftime("%Y-%m-%d")
        
        for existing_entry in self.entries:
            existing_date = existing_entry.date if isinstance(existing_entry.date, str) else existing_entry.date.strftime("%Y-%m-%d")
            if existing_date == date_str:
                return False, f"Entri untuk tanggal {date_str} sudah ada. Silakan edit entri yang sudah ada."
        
        self.entries.append(entry)
        self.entries.sort(key=lambda x: x.date if isinstance(x.date, str) else x.date.strftime("%Y-%m-%d"), reverse=True)
        self.save_entries()
        return True, "Entri berhasil ditambahkan"
    
    def update_entry(self, date, mood, journal_entry):
        date_str = date if isinstance(date, str) else date.strftime("%Y-%m-%d")
        
        for entry in self.entries:
            entry_date = entry.date if isinstance(entry.date, str) else entry.date.strftime("%Y-%m-%d")
            if entry_date == date_str:
                entry.update_mood(mood)
                entry.update_journal(journal_entry)
                self.save_entries()
                return True, "Entri berhasil diperbarui"
        
        return False, f"Tidak ada entri untuk tanggal {date_str}"
    
    def delete_entry(self, date):
        date_str = date if isinstance(date, str) else date.strftime("%Y-%m-%d")
        
        initial_count = len(self.entries)
        self.entries = [entry for entry in self.entries if 
                        (entry.date if isinstance(entry.date, str) else entry.date.strftime("%Y-%m-%d")) != date_str]
        
        if len(self.entries) < initial_count:
            self.save_entries()
            return True, "Entri berhasil dihapus"
        
        return False, f"Tidak ada entri untuk tanggal {date_str}"
    
    def get_all_entries(self):
        return self.entries
    
    def get_entry_by_date(self, date):
        date_str = date if isinstance(date, str) else date.strftime("%Y-%m-%d")
        
        for entry in self.entries:
            entry_date = entry.date if isinstance(entry.date, str) else entry.date.strftime("%Y-%m-%d")
            if entry_date == date_str:
                return entry
        
        return None 