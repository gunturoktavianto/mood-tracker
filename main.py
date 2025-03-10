import streamlit as st
from datetime import datetime
from libs import MoodEntry, MoodJournal

st.set_page_config(
    page_title="Jurnal Refleksi Harian",
    page_icon="📔",
    layout="wide"
)

if "mood_journal" not in st.session_state:
    st.session_state.mood_journal = MoodJournal()

MOOD_OPTIONS = [
    "Sangat Bahagia", "Bahagia", "Netral", "Sedih", "Sangat Sedih",
    "Stres", "Cemas", "Tenang", "Bersemangat"
]

st.title("📔 Jurnal Refleksi Harian")

page = st.sidebar.selectbox(
    "📌 Menu", 
    ["➕ Tambah Entri", "📖 Lihat Entri", "🗑️ Hapus Entri"]
)

if page == "➕ Tambah Entri":
    st.header("Tambah Entri Baru")
    st.write("Catat mood dan refleksi harianmu untuk melacak kesehatan mentalmu.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        date = st.date_input("📅 Tanggal", datetime.now())
        mood = st.selectbox("😊 Mood", MOOD_OPTIONS)
    
    journal_entry = st.text_area(
        "✏️ Catatan Harian", 
        height=200, 
        placeholder="Bagaimana perasaanmu hari ini? Apa yang terjadi?"
    )
    
    if st.button("💾 Simpan Entri", type="primary"):
        date_str = date.strftime("%Y-%m-%d")
        journal_text = journal_entry if journal_entry and journal_entry.strip() else " "
        new_entry = MoodEntry(date_str, mood, journal_text)
        success, message = st.session_state.mood_journal.add_entry(new_entry)
        
        if success:
            st.success("✅ Entri berhasil disimpan!")
            st.balloons()
        else:
            st.error(message)

elif page == "📖 Lihat Entri":
    st.header("Lihat Entri")
    st.write("Lihat dan refleksikan perjalanan mood dan pikiranmu.")
    
    entries = st.session_state.mood_journal.get_all_entries()
    
    if not entries:
        st.info("📝 Belum ada entri yang disimpan. Tambahkan entri baru untuk mulai melacak mood dan refleksimu!")
    else:
        for entry in entries:
            with st.expander(f"{entry.get_formatted_date()} - {entry.mood}"):
                st.write(f"**Mood:** {entry.mood}")
                st.write(f"**Catatan:**")
                st.write(entry.journal_entry)

elif page == "🗑️ Hapus Entri":
    st.header("Hapus Entri")
    st.write("Hapus entri yang tidak ingin kamu simpan lagi.")
    
    entries = st.session_state.mood_journal.get_all_entries()
    
    if not entries:
        st.info("📝 Belum ada entri yang disimpan.")
    else:
        dates = [(entry.date if isinstance(entry.date, str) else entry.date.strftime("%Y-%m-%d")) for entry in entries]
        date_labels = [entry.get_formatted_date() for entry in entries]
        
        label_to_date = {label: date for label, date in zip(date_labels, dates)}
        
        selected_date_label = st.selectbox(
            "📅 Pilih Tanggal untuk Dihapus",
            date_labels
        )
        
        selected_date = label_to_date[selected_date_label]
        
        selected_entry = st.session_state.mood_journal.get_entry_by_date(selected_date)
        
        if selected_entry:
            st.write(f"**Mood:** {selected_entry.mood}")
            st.write(f"**Catatan:**")
            st.write(selected_entry.journal_entry)
            
            if st.button("🗑️ Hapus Entri", type="primary"):
                success, message = st.session_state.mood_journal.delete_entry(selected_date)
                if success:
                    st.toast("✅ Entri berhasil dihapus!", icon="✅")
                    st.rerun()
                else:
                    st.error(message) 